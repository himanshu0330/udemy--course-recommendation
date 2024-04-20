# main
import streamlit as st
import pandas as pd
import pickle

# Function to recommend courses
def recommend_course(title, records=5):
    idx = course_indices[title]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    selected_course_indices = [i[0] for i in sorted_scores[1:] if i[0] < len(courseDF)]
    result = courseDF['course_title'].iloc[selected_course_indices]
    return result.head(records)


# Load the course data and similarity
courseDF = pickle.load(open('courses_main.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Extract course titles from the course dictionary
course_titles = courseDF['course_title'].values

# Get Course ID/Index
course_indices = pd.Series(courseDF.index, index=courseDF['course_title']).drop_duplicates()

# Streamlit app
st.title("Udemy - Course Recommender Engine")

# Selectbox for course selection
selected_course_name = st.selectbox(
    'Select a course:',
    course_titles
)

if st.button('Recommend'):
    recommendations = recommend_course(selected_course_name)
    for course_title in recommendations:
        st.write(course_title)
