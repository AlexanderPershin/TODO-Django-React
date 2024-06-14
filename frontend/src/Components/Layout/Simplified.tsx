import React from "react";
import { Link } from "react-router-dom";
import { Layout } from "antd";
import { HomeOutlined } from "@ant-design/icons";
import AnimatedOutlet from "../AnimatedOutlet";

const { Header, Footer, Content } = Layout;

const headerStyle: React.CSSProperties = {
    textAlign: "center",
    color: "#000",
    height: 64,
    paddingInline: 48,
    lineHeight: "64px",
    backgroundColor: "transparent",
};

const contentStyle: React.CSSProperties = {
    textAlign: "center",
    minHeight: "100%",
    lineHeight: "120px",
    color: "#000",
    backgroundColor: "transparent",
};

const footerStyle: React.CSSProperties = {
    textAlign: "center",
    color: "#000",
    backgroundColor: "transparent",
};

const layoutStyle = {
    overflow: "auto",
    width: "100%",
    maxWidth: "100vw",
    minHeight: "100vh",
    padding: "1rem",
};

const Simplified = () => {
    return (
        <Layout style={layoutStyle}>
            <Header style={headerStyle}>
                <Link to="/">
                    <HomeOutlined />
                </Link>{" "}
                Stack: Django React Docker
            </Header>
            <Content style={contentStyle}>
                <AnimatedOutlet />
            </Content>
            <Footer style={footerStyle}>
                &copy; All rights reserved, Alexander Pershin,{" "}
                {new Date().getFullYear()}
            </Footer>
        </Layout>
    );
};

export default Simplified;
