import React, { useState } from "react";
import Button from "@mui/material/Button";
import styled from "styled-components";

const Header = (props) => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [username, setUsername] = useState("testName");

    const loginPressHandler = () => {
        setIsLoggedIn(true);
    };

    const logoutPressHandler = () => {
        setIsLoggedIn(false);
    };
    return (
        <styles.containerDiv>
            {!isLoggedIn ? (
                <Button onClick={loginPressHandler} variant='contained'>
                    Login
                </Button>
            ) : (
                <Button onClick={logoutPressHandler} variant='contained'>
                    Log Out
                </Button>
            )}
            <h2>EazyLearnLogoHere</h2>
            <p>{isLoggedIn ? "Welcome back, " + username + "!" : "Welcome!"}</p>
        </styles.containerDiv>
    );
};

export default Header;

const styles = {
    containerDiv: styled.div`
        display: flex;
        width: 100%;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
        padding: 20px;
        border-bottom: 2px solid rgb(200, 200, 200);
    `,
};
