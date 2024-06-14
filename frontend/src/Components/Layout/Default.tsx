import { useLocation, useNavigate } from "react-router-dom";
import { Layout, Menu, theme } from "antd";
import {
    AppstoreOutlined,
    DashboardOutlined,
    UserOutlined,
    LogoutOutlined,
} from "@ant-design/icons";
import type { MenuProps } from "antd";

import AnimatedOutlet from "../AnimatedOutlet";

const { Header, Footer, Content } = Layout;

const menuItems = [
    {
        key: "/todos",
        label: "Dashboard",
        icon: <DashboardOutlined />,
    },

    {
        icon: <AppstoreOutlined />,
        key: "/todos/all",
        label: "Todos",
    },
    {
        icon: <UserOutlined />,
        key: "/user/profile",
        label: "Profile",
    },
    {
        icon: <LogoutOutlined />,
        key: "logout",
        label: "Sign out",
    },
];

const logoStyle: any = {
    width: "120px",
    minWidth: "120px",
    height: "32px",
    background: "#fff3",
    borderRadius: "6px",
    marginInlineEnd: "24px",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    color: "#fff",
    userSelect: "none",
};

const layoutStyle: any = {
    minHeight: "100vh",
    overflowX: "hidden",
};

const Default = () => {
    const location = useLocation();
    const navigate = useNavigate();

    const {
        token: { colorBgContainer, borderRadiusLG },
    } = theme.useToken();

    const onClick: MenuProps["onClick"] = (e) => {
        if (e.key === "logout") {
            e.domEvent.preventDefault();
            console.log("TODO: Log out user");
            return;
        }
        navigate(e.key);
    };

    return (
        <Layout style={layoutStyle}>
            <Header style={{ display: "flex", alignItems: "center" }}>
                <div style={logoStyle}>TODO App</div>

                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={[location.pathname]}
                    items={menuItems}
                    style={{ flex: 1, minWidth: 0 }}
                    onClick={onClick}
                />
            </Header>
            <Content
                style={{
                    padding: "0 48px",
                    display: "flex",
                    flexDirection: "column",
                }}
            >
                <div style={{ margin: "16px 0" }} />

                <div
                    style={{
                        background: colorBgContainer,
                        minHeight: 280,
                        padding: 24,
                        borderRadius: borderRadiusLG,
                        flexGrow: 1,
                    }}
                >
                    <AnimatedOutlet />
                </div>
            </Content>
            <Footer style={{ textAlign: "center" }}>
                &copy; {new Date().getFullYear()}, Alexander Pershin, all rights
                reserverd
            </Footer>
        </Layout>
    );
};

export default Default;
