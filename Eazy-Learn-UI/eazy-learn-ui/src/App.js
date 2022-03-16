import styled from "styled-components";
import Courses from "./components/Courses/Courses";
import { useEffect, useState } from "react";

const API_KEY = "p3Ss1kYbt7ZbRe8jkLdDAKH9LMGYXhRT";
const SEARCH_TERM = "learn";

const App = () => {
    const [chosenCourses, setChosenCourses] = useState();
    JSON.parse(window.visibleCourses);
    // [
    //     {
    //         title: "Test Course One. some padding text bla bla",
    //         link: "course_link_here",
    //         image: "#",
    //     },
    //     {
    //         title: "2Test Course One. some padding text bla bla",
    //         link: "course_link_here",
    //         image: "#",
    //     },
    //     {
    //         title: "3Test Course One. some padding text bla bla",
    //         link: "course_link_here",
    //         image: "#",
    //     },
    // ]

    useEffect(() => {
        const getGIF = async () => {
            const result = await fetch(
                `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${SEARCH_TERM}&limit=${chosenCourses.length}`
            );
            const resultJSON = await result.json();
            console.log(resultJSON);

            setChosenCourses((prev) =>
                prev.map((course, idx) => ({
                    ...course,
                    image: resultJSON.data[idx].images.original.url,
                }))
            );
        };

        getGIF();
    }, []);
    // visibleCourses is set by the python script in the window object.
    // const chosenCourses = JSON.parse(window.visibleCoures);

    // for (let i; i < chosenCourses.length; i++) {
    //     chosenCourses[i].image = "https://picsum.photos/500/400";
    // }

    // chosenCourses = [
    //     {
    //         title: "Test Course One. some padding text bla bla",
    //         link: "course_link_here",
    //         image: `api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${SEARCH_TERM}`,
    //     },
    // ];

    return (
        <Styles.AppContainer>
            <Courses chosenCourses={chosenCourses} />
        </Styles.AppContainer>
    );
};

export default App;

const Styles = {
    AppContainer: styled.div`
        padding: 20px;
    `,
};
