import React from "react";
import styled from "styled-components";

const Course = (props) => {
    const courseClickHandler = () => {
        props.onCourseClick(props.link);
    };

    return (
        <Styles.CourseContainer onClick={courseClickHandler}>
            <Styles.Image src={props.image} />
            <Styles.Title>{props.title}</Styles.Title>
        </Styles.CourseContainer>
    );
};

export default Course;

const Styles = {
    Image: styled.img`
        width: 95%;
        margin: 0 auto;
    `,

    Title: styled.p`
        padding: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 30px;
    `,

    CourseContainer: styled.div`
        display: flex;
        flex-direction: column;
        padding: 20px;
        border-radius: 15px;
        width: 100%;
        box-shadow: 1.1px 1.1px 2.2px rgba(0, 0, 0, 0.02),
            2.5px 2.5px 5.3px rgba(0, 0, 0, 0.028),
            4.8px 4.8px 10px rgba(0, 0, 0, 0.035),
            8.5px 8.5px 17.9px rgba(0, 0, 0, 0.042),
            15.9px 15.9px 33.4px rgba(0, 0, 0, 0.05),
            38px 38px 80px rgba(0, 0, 0, 0.07);

        &:hover {
            box-shadow: 1.1px 1.1px 2.2px rgba(0, 0, 0, 0.047),
                2.5px 2.5px 5.3px rgba(0, 0, 0, 0.059),
                4.8px 4.8px 10px rgba(0, 0, 0, 0.064),
                8.5px 8.5px 17.9px rgba(0, 0, 0, 0.067),
                15.9px 15.9px 33.4px rgba(0, 0, 0, 0.069),
                38px 38px 80px rgba(0, 0, 0, 0.07);
        }
    `,
};
