import React from "react";
import ReactDOM from "react-dom/client";
import {
    createHashRouter,
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";

import "./style.css";

import App from "./App.tsx";
import ErrorPage from "./ErrorPage.tsx";
import Login from "./Pages/Login.tsx";
import Simplified from "./Components/Layout/Simplified.tsx";
import Default from "./Components/Layout/Default.tsx";
import Todos from "./Pages/Todos.tsx";
import Welcome from "./Pages/Welcome.tsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Simplified />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <App />,
                errorElement: <ErrorPage />,
            },
            {
                path: "/login",
                element: <Login />,
                errorElement: <ErrorPage />,
            },
        ],
    },
    {
        path: "/todos",
        element: <Default />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/todos",
                element: <Welcome />,
                errorElement: <ErrorPage />,
            },
            {
                path: "/todos/all",
                element: <Todos />,
                errorElement: <ErrorPage />,
            },
        ],
    },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);
