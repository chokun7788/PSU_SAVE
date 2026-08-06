# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-07-31T17:10:42
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 11

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 91.18% | 98.06 | 1.6154 | 8.2408 | 12.9238 | 9 |
| 2 | llm_scb10x_llama3.2-typhoon2-3b-instruct | scb10x/llama3.2-typhoon2-3b-instruct | 88.24% | 97.59 | 1.6568 | 7.6505 | 13.7547 | 9 |
| 3 | llm_qwen3_8b | qwen3:8b | 91.18% | 97.47 | 3.9234 | 17.4288 | 31.0378 | 9 |
| 4 | llm_qwen2.5_7b | qwen2.5:7b | 88.24% | 97.29 | 2.7487 | 12.4723 | 26.3079 | 9 |
| 5 | llm_qwen3_4b | qwen3:4b | 88.24% | 97.29 | 3.0074 | 10.9457 | 20.3503 | 9 |
| 6 | llm_scb10x_llama3.1-typhoon2-8b-instruct | scb10x/llama3.1-typhoon2-8b-instruct | 88.24% | 97.24 | 3.6175 | 15.521 | 32.3055 | 9 |
| 7 | no_llm | No-LLM | 85.29% | 97.12 | 0.2071 | 0.7069 | 1.9267 | 7 |
| 8 | llm_llama3.1_8b | llama3.1:8b | 85.29% | 96.76 | 3.5423 | 14.6532 | 30.044 | 9 |
| 9 | llm_qwen2.5_3b | qwen2.5:3b | 82.35% | 96.47 | 1.8532 | 8.3492 | 12.4075 | 9 |
| 10 | llm_sailor2_8b | sailor2:8b | 88.24% | 96.26 | 4.2739 | 16.0565 | 35.3175 | 9 |
| 11 | llm_scb10x_typhoon2.1-gemma3-4b | scb10x/typhoon2.1-gemma3-4b | 85.29% | 90.06 | 12.5767 | 21.5377 | 40.1729 | 9 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 4.5735 | 8.2408 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 0.6159 | 1.0084 |
| availability_game | 2 | 100.0% | 100.0 | 1.1352 | 2.1905 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0093 | 0.0097 |
| availability_service | 2 | 50.0% | 83.0 | 0.4475 | 0.8828 |
| competition_rules | 2 | 100.0% | 100.0 | 0.7103 | 1.3595 |
| compound | 2 | 100.0% | 100.0 | 0.7728 | 0.856 |
| equipment | 2 | 100.0% | 100.0 | 0.8694 | 0.8943 |
| game_controls | 2 | 100.0% | 100.0 | 0.1498 | 0.1791 |
| game_detail | 2 | 100.0% | 100.0 | 1.0795 | 1.2181 |
| games | 2 | 100.0% | 100.0 | 0.9223 | 0.9233 |
| general_llm | 2 | 100.0% | 100.0 | 10.7166 | 12.9238 |
| members | 2 | 100.0% | 100.0 | 3.6324 | 6.1222 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0673 | 0.0863 |
| reservation | 2 | 100.0% | 100.0 | 1.7314 | 2.3013 |
| schedule | 2 | 100.0% | 100.0 | 0.0158 | 0.0177 |
| service_fee | 2 | 100.0% | 100.0 | 0.0131 | 0.0188 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1

### llm_scb10x_llama3.2-typhoon2-3b-instruct (scb10x/llama3.2-typhoon2-3b-instruct)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 4.567 | 8.1204 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 0.6474 | 1.0808 |
| availability_game | 2 | 100.0% | 100.0 | 1.2436 | 2.4159 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0101 | 0.0114 |
| availability_service | 2 | 50.0% | 83.0 | 0.5213 | 1.0288 |
| competition_rules | 2 | 100.0% | 100.0 | 0.7508 | 1.4505 |
| compound | 2 | 100.0% | 100.0 | 0.8721 | 1.0608 |
| equipment | 2 | 100.0% | 100.0 | 0.9367 | 0.9439 |
| game_controls | 2 | 100.0% | 100.0 | 0.141 | 0.1581 |
| game_detail | 2 | 100.0% | 100.0 | 1.0774 | 1.1495 |
| games | 2 | 100.0% | 100.0 | 0.9763 | 0.9975 |
| general_llm | 2 | 50.0% | 92.0 | 10.7026 | 13.7547 |
| members | 2 | 100.0% | 100.0 | 3.815 | 6.3554 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0765 | 0.0996 |
| reservation | 2 | 100.0% | 100.0 | 1.7994 | 2.3659 |
| schedule | 2 | 100.0% | 100.0 | 0.0178 | 0.0184 |
| service_fee | 2 | 100.0% | 100.0 | 0.0109 | 0.0145 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1
- `missing_any:latency|หน่วง`: 1

### llm_qwen3_8b (qwen3:8b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 95.0 | 17.8681 | 20.3699 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 1.1811 | 2.1483 |
| availability_game | 2 | 100.0% | 100.0 | 1.7694 | 3.4566 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0097 | 0.01 |
| availability_service | 2 | 50.0% | 83.0 | 1.0732 | 2.134 |
| competition_rules | 2 | 100.0% | 100.0 | 1.3284 | 2.6059 |
| compound | 2 | 100.0% | 100.0 | 1.4762 | 2.1821 |
| equipment | 2 | 100.0% | 100.0 | 2.0517 | 2.0651 |
| game_controls | 2 | 100.0% | 100.0 | 0.1553 | 0.1712 |
| game_detail | 2 | 100.0% | 100.0 | 2.3578 | 2.5241 |
| games | 2 | 100.0% | 100.0 | 2.194 | 2.2187 |
| general_llm | 2 | 100.0% | 95.0 | 24.2333 | 31.0378 |
| members | 2 | 100.0% | 100.0 | 8.051 | 13.8321 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0713 | 0.0958 |
| reservation | 2 | 100.0% | 100.0 | 2.8492 | 3.3586 |
| schedule | 2 | 100.0% | 100.0 | 0.0162 | 0.0185 |
| service_fee | 2 | 100.0% | 100.0 | 0.0112 | 0.0141 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1

### llm_qwen2.5_7b (qwen2.5:7b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 6.971 | 12.4723 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 0.9804 | 1.7356 |
| availability_game | 2 | 100.0% | 100.0 | 1.46 | 2.8479 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0102 | 0.0108 |
| availability_service | 2 | 50.0% | 83.0 | 0.7124 | 1.4088 |
| competition_rules | 2 | 100.0% | 100.0 | 1.0306 | 2.0093 |
| compound | 2 | 100.0% | 100.0 | 1.1983 | 1.6607 |
| equipment | 2 | 100.0% | 100.0 | 1.4327 | 1.4664 |
| game_controls | 2 | 100.0% | 100.0 | 0.1676 | 0.1854 |
| game_detail | 2 | 100.0% | 100.0 | 1.6656 | 1.8335 |
| games | 2 | 100.0% | 100.0 | 1.5238 | 1.5277 |
| general_llm | 2 | 50.0% | 87.0 | 20.1441 | 26.3079 |
| members | 2 | 100.0% | 100.0 | 6.99 | 12.2225 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0733 | 0.0991 |
| reservation | 2 | 100.0% | 100.0 | 2.3415 | 2.881 |
| schedule | 2 | 100.0% | 100.0 | 0.017 | 0.0192 |
| service_fee | 2 | 100.0% | 100.0 | 0.0105 | 0.0123 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1
- `missing_any:latency|หน่วง`: 1

### llm_qwen3_4b (qwen3:4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 6.8665 | 10.9457 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 1.4613 | 2.7312 |
| availability_game | 2 | 100.0% | 100.0 | 2.0781 | 4.0558 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0113 | 0.0116 |
| availability_service | 2 | 50.0% | 83.0 | 1.3347 | 2.6514 |
| competition_rules | 2 | 100.0% | 100.0 | 1.6633 | 3.2521 |
| compound | 2 | 100.0% | 100.0 | 1.9085 | 2.9382 |
| equipment | 2 | 100.0% | 100.0 | 2.7493 | 2.7531 |
| game_controls | 2 | 100.0% | 100.0 | 0.1626 | 0.1915 |
| game_detail | 2 | 100.0% | 100.0 | 2.9267 | 2.9854 |
| games | 2 | 100.0% | 100.0 | 2.7946 | 2.8567 |
| general_llm | 2 | 50.0% | 87.0 | 16.6168 | 20.3503 |
| members | 2 | 100.0% | 100.0 | 6.7728 | 10.5101 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0571 | 0.0695 |
| reservation | 2 | 100.0% | 100.0 | 3.6952 | 4.3608 |
| schedule | 2 | 100.0% | 100.0 | 0.0163 | 0.0182 |
| service_fee | 2 | 100.0% | 100.0 | 0.0108 | 0.0145 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1
- `missing_any:เฟรม|ความละเอียด`: 1

### llm_scb10x_llama3.1-typhoon2-8b-instruct (scb10x/llama3.1-typhoon2-8b-instruct)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 8.9847 | 15.342 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 1.5183 | 2.7936 |
| availability_game | 2 | 50.0% | 91.0 | 2.3921 | 4.2144 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.014 | 0.0167 |
| availability_service | 2 | 50.0% | 83.0 | 1.2089 | 2.4042 |
| competition_rules | 2 | 100.0% | 100.0 | 1.4632 | 2.8751 |
| compound | 2 | 100.0% | 100.0 | 1.5349 | 2.3927 |
| equipment | 2 | 100.0% | 100.0 | 2.33 | 2.3322 |
| game_controls | 2 | 100.0% | 100.0 | 0.154 | 0.1712 |
| game_detail | 2 | 100.0% | 100.0 | 2.4538 | 2.5055 |
| games | 2 | 100.0% | 100.0 | 2.2654 | 2.3344 |
| general_llm | 2 | 100.0% | 95.0 | 24.4114 | 32.3055 |
| members | 2 | 100.0% | 100.0 | 9.1277 | 15.521 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0683 | 0.0854 |
| reservation | 2 | 100.0% | 100.0 | 3.542 | 4.3245 |
| schedule | 2 | 100.0% | 100.0 | 0.0176 | 0.0197 |
| service_fee | 2 | 100.0% | 100.0 | 0.0115 | 0.0149 |

Top errors:
- `category_mismatch:equipment`: 2
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:1 คน|คน`: 1

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 0.1497 | 0.2893 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 0.0891 | 0.1459 |
| availability_game | 2 | 100.0% | 100.0 | 0.6159 | 1.1672 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0091 | 0.0094 |
| availability_service | 2 | 50.0% | 83.0 | 0.0237 | 0.036 |
| competition_rules | 2 | 100.0% | 100.0 | 0.216 | 0.3921 |
| compound | 2 | 100.0% | 100.0 | 0.3665 | 0.7069 |
| equipment | 2 | 100.0% | 100.0 | 0.0281 | 0.0464 |
| game_controls | 2 | 100.0% | 100.0 | 0.1117 | 0.1282 |
| game_detail | 2 | 100.0% | 100.0 | 0.1023 | 0.1306 |
| games | 2 | 100.0% | 100.0 | 0.0993 | 0.1043 |
| general_llm | 2 | 0.0% | 84.0 | 0.1475 | 0.1491 |
| members | 2 | 100.0% | 100.0 | 0.2811 | 0.4253 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.076 | 0.0954 |
| reservation | 2 | 100.0% | 100.0 | 1.1677 | 1.9267 |
| schedule | 2 | 100.0% | 100.0 | 0.0208 | 0.025 |
| service_fee | 2 | 100.0% | 100.0 | 0.0158 | 0.0219 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1
- `missing_any:latency|หน่วง`: 1
- `missing_any:เฟรม|ความละเอียด`: 1

### llm_llama3.1_8b (llama3.1:8b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 8.6824 | 14.6532 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 1.5662 | 2.9352 |
| availability_game | 2 | 50.0% | 91.0 | 2.2096 | 3.8835 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0146 | 0.015 |
| availability_service | 2 | 50.0% | 83.0 | 1.0164 | 2.0183 |
| competition_rules | 2 | 100.0% | 100.0 | 1.7118 | 3.3412 |
| compound | 2 | 100.0% | 100.0 | 1.8332 | 2.8378 |
| equipment | 2 | 100.0% | 100.0 | 2.8998 | 2.9009 |
| game_controls | 2 | 100.0% | 100.0 | 0.1619 | 0.1898 |
| game_detail | 2 | 100.0% | 100.0 | 2.8262 | 2.8868 |
| games | 2 | 100.0% | 100.0 | 2.4127 | 2.7625 |
| general_llm | 2 | 50.0% | 87.0 | 23.3175 | 30.044 |
| members | 2 | 100.0% | 100.0 | 8.0937 | 13.9673 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0712 | 0.0917 |
| reservation | 2 | 100.0% | 100.0 | 3.3757 | 3.9018 |
| schedule | 2 | 100.0% | 100.0 | 0.017 | 0.0191 |
| service_fee | 2 | 100.0% | 100.0 | 0.0097 | 0.0123 |

Top errors:
- `category_mismatch:equipment`: 2
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:1 คน|คน`: 1
- `missing_any:latency|หน่วง`: 1

### llm_qwen2.5_3b (qwen2.5:3b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 4.5945 | 8.3492 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 0.5854 | 0.941 |
| availability_game | 2 | 50.0% | 91.0 | 1.1926 | 1.9169 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0097 | 0.0104 |
| availability_service | 2 | 50.0% | 83.0 | 0.3814 | 0.7505 |
| competition_rules | 2 | 100.0% | 100.0 | 0.7079 | 1.367 |
| compound | 2 | 100.0% | 100.0 | 0.9129 | 0.9726 |
| equipment | 2 | 100.0% | 100.0 | 0.8331 | 0.8768 |
| game_controls | 2 | 100.0% | 100.0 | 0.1648 | 0.1944 |
| game_detail | 2 | 100.0% | 100.0 | 1.0878 | 1.1812 |
| games | 2 | 100.0% | 100.0 | 0.8472 | 0.8561 |
| general_llm | 2 | 100.0% | 100.0 | 10.2696 | 12.4075 |
| members | 2 | 100.0% | 100.0 | 4.1662 | 7.235 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0675 | 0.0907 |
| reservation | 2 | 0.0% | 82.0 | 5.6545 | 9.3367 |
| schedule | 2 | 100.0% | 100.0 | 0.0173 | 0.0197 |
| service_fee | 2 | 100.0% | 100.0 | 0.0114 | 0.0139 |

Top errors:
- `category_mismatch:equipment`: 4
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:1 คน|คน`: 1

### llm_sailor2_8b (sailor2:8b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 100.0 | 9.8008 | 16.0565 |
| ambiguous_controls | 2 | 100.0% | 100.0 | 1.8559 | 3.4799 |
| availability_game | 2 | 100.0% | 100.0 | 2.2012 | 4.3045 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0132 | 0.0144 |
| availability_service | 2 | 50.0% | 83.0 | 1.4622 | 2.906 |
| competition_rules | 2 | 100.0% | 100.0 | 1.9678 | 3.8859 |
| compound | 2 | 100.0% | 100.0 | 1.994 | 3.3053 |
| equipment | 2 | 100.0% | 100.0 | 3.3368 | 3.3757 |
| game_controls | 2 | 100.0% | 100.0 | 0.1618 | 0.1786 |
| game_detail | 2 | 100.0% | 100.0 | 3.2631 | 3.2769 |
| games | 2 | 100.0% | 100.0 | 2.915 | 2.9219 |
| general_llm | 2 | 50.0% | 69.5 | 28.9747 | 35.3175 |
| members | 2 | 100.0% | 100.0 | 9.6383 | 15.6654 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0769 | 0.1008 |
| reservation | 2 | 100.0% | 100.0 | 4.9604 | 5.4 |
| schedule | 2 | 100.0% | 100.0 | 0.017 | 0.0184 |
| service_fee | 2 | 100.0% | 100.0 | 0.0163 | 0.0222 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1
- `missing_any:เฟรม|ความละเอียด`: 1
- `llm_required_but_unavailable`: 1

### llm_scb10x_typhoon2.1-gemma3-4b (scb10x/typhoon2.1-gemma3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 2 | 100.0% | 90.0 | 20.1854 | 20.3474 |
| ambiguous_controls | 2 | 100.0% | 95.0 | 10.1412 | 20.0559 |
| availability_game | 2 | 100.0% | 95.0 | 10.7476 | 21.4218 |
| availability_machine_split | 2 | 0.0% | 84.0 | 0.0098 | 0.0101 |
| availability_service | 2 | 50.0% | 78.0 | 10.0324 | 20.0531 |
| competition_rules | 2 | 100.0% | 95.0 | 10.3085 | 20.5659 |
| compound | 2 | 100.0% | 95.0 | 10.3419 | 20.0449 |
| equipment | 2 | 100.0% | 90.0 | 20.0533 | 20.084 |
| game_controls | 2 | 100.0% | 100.0 | 0.1633 | 0.1882 |
| game_detail | 2 | 100.0% | 90.0 | 20.1478 | 20.1953 |
| games | 2 | 100.0% | 90.0 | 20.1441 | 20.1452 |
| general_llm | 2 | 0.0% | 49.0 | 40.1688 | 40.1729 |
| members | 2 | 100.0% | 90.0 | 20.2668 | 20.3859 |
| policy_schedule_rules | 2 | 100.0% | 100.0 | 0.0706 | 0.0942 |
| reservation | 2 | 100.0% | 90.0 | 20.9894 | 21.5377 |
| schedule | 2 | 100.0% | 100.0 | 0.0209 | 0.0225 |
| service_fee | 2 | 100.0% | 100.0 | 0.0114 | 0.0155 |

Top errors:
- `missing_any:ไม่มี|PC #03-#10`: 2
- `llm_required_but_unavailable`: 2
- `category_mismatch:equipment`: 1
- `missing_any:1 คน|คน`: 1
- `missing_any:latency|หน่วง`: 1
- `missing_any:เฟรม|ความละเอียด`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
