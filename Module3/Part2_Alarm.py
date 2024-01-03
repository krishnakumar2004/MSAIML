# Calculate No of Hour alarm goes off in 24Hour clock
# Get first input as time now in hours
# assign to variable current_Time
# Get second input as  No of hours to set alarm off
# assign to variable alarm_set_off_hours
# calculate and assign to output variable alarm_goes_off_at

current_Time = int(input('Enter current time in hours : \n'))
alarm_set_off_hours = int(input('Enter no of hours to set alarm off : \n'))
# use modulus operand to get remaining hours
alarm_goes_off_at = (current_Time + alarm_set_off_hours) % 24
# format output as whole number13

print('On 24-hour clock alarm goes off @ {:.0f} Hour'.format(alarm_goes_off_at))
