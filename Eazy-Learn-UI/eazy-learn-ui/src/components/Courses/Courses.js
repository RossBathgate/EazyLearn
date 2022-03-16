import React from "react";
import styled from "styled-components";
import Course from "./Course";

const Courses = (props) => {
    const courseClickHandler = (link) => {
        window.location.href = link;
    };

    return (
        <Styles.CoursesContainer>
            {props.chosenCourses &&
                props.chosenCourses.map((course) => (
                    <Course
                        title={course.title}
                        link={course.link}
                        image={course.image}
                        key={course.title}
                        onCourseClick={courseClickHandler}
                    />
                ))}
        </Styles.CoursesContainer>
    );
};

export default Courses;

const Styles = {
    CoursesContainer: styled.div`
        padding: 20px;
        display: grid;
        grid-template-columns: auto auto auto;
        row-gap: 50px;
        column-gap: 50px;

        @media (max-width: 1000px) {
            grid-template-columns: auto;
        }
    `,
};
