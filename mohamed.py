import streamlit as st
def calculate_mean_grades(grades):
    total_grades = sum(grades)
    num_subjects = len(grades)
    mean_grade = total_grades / num_subjects
    return mean_grade
def main():
    st.title("Student Grade Calculator")
    st.write("Enter the grades for each subject:")
    num_subjects = st.number_input("Number of subjects", min_value=1, max_value=10, value=1, step=1)
    grades = []
    for i in range(num_subjects):
        grade = st.number_input(f"Grade for subject {i+1}", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        grades.append(grade)
    if st.button("Calculate Mean"):
        mean_grade = calculate_mean_grades(grades)
        st.write(f"The mean grade is: {mean_grade}")
if __name__ == "__main__":
    main()