function Test-BookingDashboardIdentity {
    param([string]$BaseUrl = "http://127.0.0.1:8080")
    try {
        $schedule = Invoke-RestMethod -Uri "$($BaseUrl.TrimEnd('/'))/api/center-schedule" -TimeoutSec 2
        return $schedule.ok -eq $true -and $null -ne $schedule.schedule.weekly
    } catch {
        return $false
    }
}

function Get-BookingDashboardProbe {
    param([string]$BaseUrl = "http://127.0.0.1:8091")

    $base = $BaseUrl.TrimEnd('/')
    try {
        $health = Invoke-RestMethod -Uri "$base/health" -TimeoutSec 2
        if ($health.ok -eq $true -and
            $health.service -eq "psu-booking-dashboard" -and
            $health.calendar_contract -eq "lunch-closed-v1") {
            return [pscustomobject]@{ Ready = $true; Kind = "contract"; Reason = "lunch-closed-v1" }
        }
    } catch {
        # The owner-operated D: Dashboard predates /health. Verify its
        # aggregate endpoint and effective lunch closure below.
    }

    try {
        # Tuesday is a normal open day. This probes effective periods without
        # reading the owner/admin endpoint or exposing appointment details.
        $status = Invoke-RestMethod -Uri "$base/api/chatbot-status?date=2026-09-29" -TimeoutSec 8
        if ($status.ok -ne $true -or
            $status.source -ne "remote_csv_live" -or
            $status.date -ne "2026-09-29" -or
            $status.center.open -ne $true -or
            $null -eq $status.resources -or
            @($status.resources).Count -lt 1 -or
            [string]::IsNullOrWhiteSpace([string]@($status.resources)[0].resource_id)) {
            return [pscustomobject]@{ Ready = $false; Kind = "legacy"; Reason = "live aggregate data is incomplete" }
        }

        $lunchClosed = $true
        $morningOpen = $false
        $afternoonOpen = $false
        foreach ($period in @($status.center.open_periods)) {
            if (@($period).Count -ne 2) {
                return [pscustomobject]@{ Ready = $false; Kind = "legacy"; Reason = "invalid opening periods" }
            }
            $start = [string]$period[0]
            $end = [string]$period[1]
            if ($start -le "12:30" -and "12:30" -lt $end) { $lunchClosed = $false }
            if ($start -le "11:00" -and "11:00" -lt $end) { $morningOpen = $true }
            if ($start -le "13:00" -and "13:00" -lt $end) { $afternoonOpen = $true }
        }
        if ($lunchClosed -and $morningOpen -and $afternoonOpen) {
            return [pscustomobject]@{ Ready = $true; Kind = "legacy-verified"; Reason = "live aggregate and lunch closure verified" }
        }
        return [pscustomobject]@{ Ready = $false; Kind = "legacy"; Reason = "opening periods do not match the confirmed lunch break" }
    } catch {
        return [pscustomobject]@{ Ready = $false; Kind = "unavailable"; Reason = "no compatible aggregate booking status" }
    }
}
