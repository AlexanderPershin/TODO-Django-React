import { useState } from "react";
import { Button, Space, DatePicker, version } from "antd";
import { Link } from "react-router-dom";

function App() {
    return (
        <div style={{ padding: "0 24px", height: "100%", width: "100%" }}>
            <Space
                direction="vertical"
                align="center"
                style={{
                    width: "100%",
                    height: "100%",
                    justifyContent: "center",
                    alignItems: "center",
                }}
            >
                <h1>TODO application</h1>
                <p>
                    Next you can <Link to="/login">Login</Link> or{" "}
                    <Link to="/register">Register</Link>{" "}
                </p>
            </Space>
        </div>
    );
}

export default App;
