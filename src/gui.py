import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys
from pathlib import Path



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import the function
from pipeline.pipeline import predict



def initialize():
    # Set appearance mode and default color theme
    ctk.set_appearance_mode("dark")  # Modes: system, light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue, green, dark-blue
    
    # Define window size and properties - same size but with scrollable content
    WIDTH, HEIGHT = 900, 700
    app = ctk.CTk()
    app.geometry(f"{WIDTH}x{HEIGHT}")
    app.title("Depression Risk Assessment Tool")
    app.resizable(True, True)  # Allow resizing
    
    # # Create main frame with scrollbar
    main_frame = ctk.CTkScrollableFrame(app, width=WIDTH-40, height=HEIGHT-40 ,bg_color="#2b2b2b")
    main_frame.pack(padx=20, pady=20, fill="both", expand=True)
    

# Variables to store user inputs
    user_data = {
        'Name': ctk.StringVar(),
        'Gender': ctk.StringVar(value="Male"),
        'Age': ctk.StringVar(),
        'City': ctk.StringVar(),
        'Working Professional or Student': ctk.StringVar(value="Student"),
        'Profession': ctk.StringVar(),
        'Academic Pressure': ctk.DoubleVar(value=3.0),
        'Work Pressure': ctk.DoubleVar(value=3.0),
        'CGPA': ctk.StringVar(),
        'Study Satisfaction': ctk.DoubleVar(value=3.0),
        'Job Satisfaction': ctk.DoubleVar(value=3.0),
        'Sleep Duration': ctk.StringVar(value="7-8 hours"),
        'Dietary Habits': ctk.StringVar(value="Moderate Diet"),
        'Degree': ctk.StringVar(),
        'Have you ever had suicidal thoughts ?': ctk.StringVar(value="No"),
        'Work/Study Hours': ctk.StringVar(),
        'Financial Stress': ctk.DoubleVar(value=3.0),
        'Family History of Mental Illness': ctk.StringVar(value="No"),
    }
    
    result_text = ctk.StringVar(value="Fill all fields and click Calculate to see results")
    
    # Function to toggle visibility of fields based on user category
    def toggle_fields():
        category = user_data['Working Professional or Student'].get()
        
        if category == "Student":
            # Show student fields, hide professional fields
            student_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
            professional_frame.grid_remove()
        else:
            # Show professional fields, hide student fields
            professional_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
            student_frame.grid_remove()
    
    # Function to validate and calculate results
    def calculate_results():
        # Reset result text
        result_text.set("Processing...")
        app.update_idletasks()
        
        # Validate basic inputs
        if not user_data['Age'].get().strip() or not user_data['Work/Study Hours'].get().strip():
            result_text.set("Please fill in all required fields")
            return
        
        # Prepare input data for prediction
        input_data = {
            'Name': user_data['Name'].get(),
            'Gender': user_data['Gender'].get(),
            'Age': float(user_data['Age'].get()),
            'City': user_data['City'].get(),
            'Working Professional or Student': user_data['Working Professional or Student'].get(),
            'Profession': user_data['Profession'].get(),
            'Sleep Duration': user_data['Sleep Duration'].get(),
            'Dietary Habits': user_data['Dietary Habits'].get(),
            'Degree': user_data['Degree'].get(),
            'Have you ever had suicidal thoughts ?': user_data['Have you ever had suicidal thoughts ?'].get(),
            'Work/Study Hours': float(user_data['Work/Study Hours'].get()),
            'Financial Stress': float(user_data['Financial Stress'].get()),
            'Family History of Mental Illness': user_data['Family History of Mental Illness'].get(),
        }
        
        # Add category-specific fields
        if user_data['Working Professional or Student'].get() == "Student":
            input_data.update({
                'Academic Pressure': float(user_data['Academic Pressure'].get()),
                'Work Pressure': None,
                'CGPA': float(user_data['CGPA'].get()) if user_data['CGPA'].get() else None,
                'Study Satisfaction': float(user_data['Study Satisfaction'].get()),
                'Job Satisfaction': None,
            })
        else:
            input_data.update({
                'Academic Pressure': None,
                'Work Pressure': float(user_data['Work Pressure'].get()),
                'CGPA': None,
                'Study Satisfaction': None,
                'Job Satisfaction': float(user_data['Job Satisfaction'].get()),
            })
        
        try:
            # Get prediction
            prediction_result = predict(input_data)
            probability = prediction_result.get("probability", 0) * 100
            
            # Set result text with color coding based on risk level
            if probability < 30:
                result_frame.configure(fg_color="#1e5631")  # Dark green for low risk
                result_text.set(f"Low Risk: {probability:.1f}% probability of depression")
            elif probability < 70:
                result_frame.configure(fg_color="#b7950b")  # Amber for medium risk
                result_text.set(f"Moderate Risk: {probability:.1f}% probability of depression")
            else:
                result_frame.configure(fg_color="#922b21")  # Dark red for high risk
                result_text.set(f"High Risk: {probability:.1f}% probability of depression")

            # Ensure the result is visible by scrolling to it
            result_frame.update()
            result_frame.tkraise()

        except Exception as e:
            result_text.set(f"Error: {str(e)}")
    
    # Create main content sections
    # 1. Header section
    header_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    header_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
    header_frame.grid_columnconfigure(0, weight=1)
    
    header_label = ctk.CTkLabel(
        header_frame, 
        text="Depression Risk Assessment Tool",
        font=ctk.CTkFont(size=24, weight="bold"),
        padx=20, pady=15
    )
    header_label.pack()
    
    # 2. Personal Information Section
    personal_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    personal_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    personal_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
    
    personal_label = ctk.CTkLabel(
        personal_frame, 
        text="Personal Information",
        font=ctk.CTkFont(size=16, weight="bold"),
        padx=20, pady=10
    )
    personal_label.grid(row=0, column=0, columnspan=4, sticky="w")
    
    # Name field
    ctk.CTkLabel(personal_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ctk.CTkEntry(personal_frame, textvariable=user_data['Name'], width=150).grid(row=1, column=1, padx=10, pady=5, sticky="w")
    
    # Age field
    ctk.CTkLabel(personal_frame, text="Age:").grid(row=1, column=2, padx=10, pady=5, sticky="e")
    ctk.CTkEntry(personal_frame, textvariable=user_data['Age'], width=70).grid(row=1, column=3, padx=10, pady=5, sticky="w")
    
    # City field
    ctk.CTkLabel(personal_frame, text="City:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    ctk.CTkEntry(personal_frame, textvariable=user_data['City'], width=150).grid(row=2, column=1, padx=10, pady=5, sticky="w")
    
    # Gender field
    ctk.CTkLabel(personal_frame, text="Gender:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
    ctk.CTkComboBox(
        personal_frame, 
        values=["Male", "Female"],
        variable=user_data['Gender'],
        width=120
    ).grid(row=2, column=3, padx=10, pady=5, sticky="w")
    
    # 3. Category Selection
    category_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    category_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    category_frame.grid_columnconfigure(0, weight=1)
    
    ctk.CTkLabel(
        category_frame, 
        text="I am a:",
        font=ctk.CTkFont(size=16, weight="bold"),
        padx=20, pady=10
    ).pack(side="left", padx=10)
    
    student_button = ctk.CTkRadioButton(
        category_frame, 
        text="Student", 
        variable=user_data['Working Professional or Student'], 
        value="Student",
        command=toggle_fields
    )
    student_button.pack(side="left", padx=20)
    
    professional_button = ctk.CTkRadioButton(
        category_frame, 
        text="Working Professional", 
        variable=user_data['Working Professional or Student'], 
        value="Working Professional",
        command=toggle_fields
    )
    professional_button.pack(side="left", padx=20)
    
    # 4. Common fields
    common_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    common_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    common_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    common_label = ctk.CTkLabel(
        common_frame, 
        text="Lifestyle Factors",
        font=ctk.CTkFont(size=16, weight="bold"),
        padx=20, pady=10
    )
    common_label.grid(row=0, column=0, columnspan=4, sticky="w")
    
    # Common fields - Row 1
    ctk.CTkLabel(common_frame, text="Sleep Duration:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ctk.CTkComboBox(
        common_frame, 
        values=["More than 8 hours", "7-8 hours", "5-6 hours", "Less than 5 hours"],
        variable=user_data['Sleep Duration'],
        width=150
    ).grid(row=1, column=1, padx=10, pady=5, sticky="w")
    
    ctk.CTkLabel(common_frame, text="Dietary Habits:").grid(row=1, column=2, padx=10, pady=5, sticky="e")
    ctk.CTkComboBox(
        common_frame, 
        values=["Healthy Diet", "Moderate Diet", "Unhealthy Diet"],
        variable=user_data['Dietary Habits'],
        width=150
    ).grid(row=1, column=3, padx=10, pady=5, sticky="w")
    
    # Common fields - Row 2
    ctk.CTkLabel(common_frame, text="Profession/Degree:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    ctk.CTkEntry(common_frame, textvariable=user_data['Degree'], width=150).grid(row=2, column=1, padx=10, pady=5, sticky="w")
    
    ctk.CTkLabel(common_frame, text="Work/Study Hours:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
    ctk.CTkEntry(common_frame, textvariable=user_data['Work/Study Hours'], width=70).grid(row=2, column=3, padx=10, pady=5, sticky="w")
    
    # Common fields - Row 3
    ctk.CTkLabel(common_frame, text="Financial Stress (1-5):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    financial_slider = ctk.CTkSlider(
        common_frame,
        from_=1, to=5,
        number_of_steps=4,
        variable=user_data['Financial Stress'],
        width=150
    )
    financial_slider.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    financial_label = ctk.CTkLabel(common_frame, textvariable=ctk.StringVar())
    user_data['Financial Stress'].trace_add("write", lambda *args: financial_label.configure(text=f"{user_data['Financial Stress'].get():.0f}"))
    financial_label.grid(row=3, column=1, padx=(160, 0), pady=5, sticky="w")
    
    # Common fields - Row 4
    ctk.CTkLabel(common_frame, text="Family History of Mental Illness:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    ctk.CTkComboBox(
        common_frame, 
        values=["Yes", "No"],
        variable=user_data['Family History of Mental Illness'],
        width=70
    ).grid(row=4, column=1, padx=10, pady=5, sticky="w")
    
    ctk.CTkLabel(common_frame, text="Suicidal Thoughts:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
    ctk.CTkComboBox(
        common_frame, 
        values=["Yes", "No"],
        variable=user_data['Have you ever had suicidal thoughts ?'],
        width=70
    ).grid(row=4, column=3, padx=10, pady=5, sticky="w")
    
    # 5. Student-specific fields
    student_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    student_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    student_frame.grid_columnconfigure((0, 1), weight=1)
    
    student_label = ctk.CTkLabel(
        student_frame, 
        text="Student Factors",
        font=ctk.CTkFont(size=16, weight="bold"),
        padx=20, pady=10
    )
    student_label.grid(row=0, column=0, columnspan=4, sticky="w")
    
    # Academic Pressure
    ctk.CTkLabel(student_frame, text="Academic Pressure (1-5):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    academic_slider = ctk.CTkSlider(
        student_frame,
        from_=1, to=5,
        number_of_steps=4,
        variable=user_data['Academic Pressure'],
        width=200
    )
    academic_slider.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    academic_label = ctk.CTkLabel(student_frame, textvariable=ctk.StringVar())
    user_data['Academic Pressure'].trace_add("write", lambda *args: academic_label.configure(text=f"{user_data['Academic Pressure'].get():.0f}"))
    academic_label.grid(row=1, column=1, padx=(210, 0), pady=10, sticky="w")
    
    # Study Satisfaction
    ctk.CTkLabel(student_frame, text="Study Satisfaction (1-5):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    study_slider = ctk.CTkSlider(
        student_frame,
        from_=1, to=5,
        number_of_steps=4,
        variable=user_data['Study Satisfaction'],
        width=200
    )
    study_slider.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    study_label = ctk.CTkLabel(student_frame, textvariable=ctk.StringVar())
    user_data['Study Satisfaction'].trace_add("write", lambda *args: study_label.configure(text=f"{user_data['Study Satisfaction'].get():.0f}"))
    study_label.grid(row=2, column=1, padx=(210, 0), pady=10, sticky="w")
    
    # CGPA
    ctk.CTkLabel(student_frame, text="CGPA:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    ctk.CTkEntry(student_frame, textvariable=user_data['CGPA'], width=100).grid(row=3, column=1, padx=10, pady=10, sticky="w")
    
    # 6. Professional-specific fields
    professional_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    professional_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    professional_frame.grid_columnconfigure((0, 1), weight=1)
    
    professional_label = ctk.CTkLabel(
        professional_frame, 
        text="Work Factors",
        font=ctk.CTkFont(size=16, weight="bold"),
        padx=20, pady=10
    )
    professional_label.grid(row=0, column=0, columnspan=4, sticky="w")
    
    # Work Pressure
    ctk.CTkLabel(professional_frame, text="Work Pressure (1-5):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    work_slider = ctk.CTkSlider(
        professional_frame,
        from_=1, to=5,
        number_of_steps=4,
        variable=user_data['Work Pressure'],
        width=200
    )
    work_slider.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    work_label = ctk.CTkLabel(professional_frame, textvariable=ctk.StringVar())
    user_data['Work Pressure'].trace_add("write", lambda *args: work_label.configure(text=f"{user_data['Work Pressure'].get():.0f}"))
    work_label.grid(row=1, column=1, padx=(210, 0), pady=10, sticky="w")
    
    # Job Satisfaction
    ctk.CTkLabel(professional_frame, text="Job Satisfaction (1-5):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    job_slider = ctk.CTkSlider(
        professional_frame,
        from_=1, to=5,
        number_of_steps=4,
        variable=user_data['Job Satisfaction'],
        width=200
    )
    job_slider.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    job_label = ctk.CTkLabel(professional_frame, textvariable=ctk.StringVar())
    user_data['Job Satisfaction'].trace_add("write", lambda *args: job_label.configure(text=f"{user_data['Job Satisfaction'].get():.0f}"))
    job_label.grid(row=2, column=1, padx=(210, 0), pady=10, sticky="w")
    
    # 7. Result and calculate button section
    button_frame = ctk.CTkFrame(main_frame, corner_radius=10)
    button_frame.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    
    calculate_button = ctk.CTkButton(
        button_frame,
        text="Calculate Risk",
        font=ctk.CTkFont(size=16, weight="bold"),
        command=calculate_results,
        height=40,
        fg_color="#2980b9",
        hover_color="#1c587f"
    )
    calculate_button.pack(pady=20)
    
    # 8. Results display
    result_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#333333")
    result_frame.grid(row=6, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")
    
    result_label = ctk.CTkLabel(
        result_frame,
        textvariable=result_text,
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color="white"
    )
    result_label.pack(pady=20)
    
    # Add disclaimer
    disclaimer_text = (
        "Disclaimer: This tool provides an estimate only and should not be used for clinical diagnosis. "
        "If you are experiencing symptoms of depression, please consult a healthcare professional."
    )
    disclaimer_label = ctk.CTkLabel(
        main_frame,
        text=disclaimer_text,
        font=ctk.CTkFont(size=10),
        text_color="#999999",
        wraplength=WIDTH-40
    )
    disclaimer_label.grid(row=7, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")
    
    # Initialize with Student view by default
    toggle_fields()
    
    # Start the application
    app.mainloop()

# Run the application
if __name__ == "__main__":
    initialize()