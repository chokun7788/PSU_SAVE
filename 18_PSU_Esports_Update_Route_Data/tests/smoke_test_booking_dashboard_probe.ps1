$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "..\deployment_templates\Booking-Dashboard-Probe.ps1")

$script:ProbeCase = ""
function Invoke-RestMethod {
    param([string]$Uri, [int]$TimeoutSec)
    if ($Uri.EndsWith("/api/center-schedule")) {
        if ($script:ProbeCase -eq "wrong-service") { return [pscustomobject]@{ ok = $true } }
        return [pscustomobject]@{ ok = $true; schedule = [pscustomobject]@{ weekly = @{ "1" = @{ open = $true } } } }
    }
    if ($Uri.EndsWith("/health")) {
        if ($script:ProbeCase -eq "contract") {
            return [pscustomobject]@{ ok = $true; service = "psu-booking-dashboard"; calendar_contract = "lunch-closed-v1" }
        }
        throw "Legacy Dashboard has no /health"
    }
    if ($script:ProbeCase -eq "offline") { throw "CSV source unavailable" }
    $periods = if ($script:ProbeCase -eq "old-lunch") {
        @(@("09:00", "16:00"))
    } else {
        @(@("09:00", "12:00"), @("13:00", "16:00"))
    }
    return [pscustomobject]@{
        ok = $true
        source = "remote_csv_live"
        date = "2026-09-29"
        center = [pscustomobject]@{ open = $true; open_periods = $periods }
        resources = @([pscustomobject]@{ resource_id = "1"; resource_name = "PC #01" })
    }
}

foreach ($case in @(
    @{ Name = "contract"; Ready = $true; Kind = "contract" },
    @{ Name = "legacy-closed-lunch"; Ready = $true; Kind = "legacy-verified" },
    @{ Name = "old-lunch"; Ready = $false; Kind = "legacy" },
    @{ Name = "offline"; Ready = $false; Kind = "unavailable" }
)) {
    $script:ProbeCase = $case.Name
    $result = Get-BookingDashboardProbe -BaseUrl "http://127.0.0.1:8091"
    if ($result.Ready -ne $case.Ready -or $result.Kind -ne $case.Kind) {
        throw "Case $($case.Name): expected $($case.Ready)/$($case.Kind), got $($result.Ready)/$($result.Kind): $($result.Reason)"
    }
}
$script:ProbeCase = "legacy-closed-lunch"
if (-not (Test-BookingDashboardIdentity -BaseUrl "http://127.0.0.1:8080")) {
    throw "Owner Dashboard identity was not recognized"
}
$script:ProbeCase = "wrong-service"
if (Test-BookingDashboardIdentity -BaseUrl "http://127.0.0.1:8080") {
    throw "Unrelated service was recognized as owner Dashboard"
}
Write-Host "Booking Dashboard probe: 6 cases passed"
