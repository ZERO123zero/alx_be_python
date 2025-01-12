# daily_reminder.py  

def daily_reminder():  
    # Prompt for task description  
    task = input("Enter your task: ")  

    # Prompt for priority  
    priority = input("Priority (high/medium/low): ").lower().strip()  

    # Prompt for time sensitivity  
    is_time_bound = input("Is it time-bound (yes/no): ").lower().strip()  

    # Determine priority messages using Match Case  
    match priority:  
        case 'high':  
            reminder_message = f"Reminder: '{task}' is a high priority task"  
            if is_time_bound == 'yes':  
                reminder_message += " that requires immediate attention today!"  
            else:  
                reminder_message += ". Consider completing it as soon as possible."  
        case 'medium':  
            reminder_message = f"Reminder: '{task}' is a medium priority task."  
            if is_time_bound == 'yes':  
                reminder_message += " It would be wise to address it soon!"  
            else:  
                reminder_message += " You can handle it when you have some time."  
        case 'low':  
            reminder_message = f"Note: '{task}' is a low priority task."  
            if is_time_bound == 'yes':  
                reminder_message += " However, please consider completing it as soon as possible."  
            else:  
                reminder_message += " Consider completing it when you have free time."  
        case _:  
            reminder_message = "Invalid priority level. Please enter 'high', 'medium', or 'low'."  

    # Print the custom reminder  
    print(reminder_message)  

# Run the reminder function  
if __name__ == "__main__":  
    daily_reminder()