| Address | Direction | Packet type | Position | n bytes | data type | name |
| --------| ----------| ------------| ---------| --------| ----------| -----|
| 00 | 00 | 10 | 00 | 1 | flag(1) | Heating_Status_Setting |
| 00 | 00 | 10 | 02 | 1 | flag(1) | DHW_Status_Setting |
| 00 | 00 | 10 | 03 | 2 | ignore | Unknown byte |
| 00 | 00 | 10 | 07 | 2 | f8s8 | DHW_Setpoint |
| 00 | 00 | 10 | 09 | 1 | flag(1) | Silent_Setting |
| 00 | 00 | 11 | 01 | 1 | ignore | Unknown byte 00 00 11 1 |
| 00 | 00 | 11 | 02 | 1 | ignore | Unknown byte 00 00 11 2 |
| 00 | 00 | 12 | 01 | 1 | u8 | Time_dow |
| 00 | 00 | 12 | 02 | 1 | u8 | Time_hours |
| 00 | 00 | 12 | 03 | 1 | u8 | Time_minutes |
| 00 | 00 | 12 | 04 | 1 | u8 | Time_seconds |
| 00 | 00 | 0D | 01 | 1 | ignore | Unknown field |
| 00 | 00 | 0D | 03 | 1 | ignore | Unknown field |
| 00 | 00 | 0D | 05 | 1 | ignore | Unknown field |
| 00 | 00 | 0D | 06 | 2 | ignore | Unknown field |
| 00 | 00 | 0D | 08 | 2 | ignore | Unknown field |
| 00 | 00 | 0D | 11 | 1 | ignore | Unknown field |
| 00 | 00 | 0D | 14 | 2 | ignore | Unknown field |
| 00 | 00 | 0E | 02 | 2 | ignore | Unknown counter |
| 00 | 40 | 10 | 00 | 1 | flag(1) | Heating_Status |
| 00 | 40 | 10 | 03 | 1 | flag(1) | DHW_Status |
| 00 | 40 | 10 | 04 | 2 | f8s8 | Target_Temperature_Leaving_Water |
| 00 | 40 | 10 | 14 | 2 | f8_8r | Temperature_outside |
| 00 | 40 | 11 | 00 | 2 | f8_8r | Unknown field |
| 00 | 40 | 11 | 02 | 2 | f8_8r | Temperature_DHW_Tank |
| 00 | 40 | 11 | 04 | 2 | f8_8r | Temperature_HP2Gas_Water |
| 00 | 40 | 11 | 06 | 2 | f8_8r | Temperature_Return_Water |
| 00 | 40 | 11 | 08 | 2 | f8_8r | Temperature_Leaving_Water |
| 00 | 40 | 11 | 10 | 2 | f8_8r | Temperature_Refrigerant_1 |
| 00 | 40 | 0D | 03 | 4 | ignore | Unknown counter |
| 00 | 40 | 0D | 09 | 1 | ignore | Unknown byte |
| 00 | 40 | 0E | 02 | 2 | ignore | Unknown counter |
| 00 | 40 | 0F | 02 | 2 | ignore | Unknown 2 bytes |
| 01 | 00 | 20 | 00 | 0 | ignore | ignore |
| 80 | 80 | 00 | 00 | 0 | ignore | ignore |
