import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { AnimatePresence } from "framer-motion";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js/pure";

import "./style.css";

import App from "./App.tsx";
import ErrorPage from "./ErrorPage.tsx";
import Login from "./Pages/Login.tsx";
import Simplified from "./Components/Layout/Simplified.tsx";
import Default from "./Components/Layout/Default.tsx";
import Todos from "./Pages/Todos.tsx";
import Welcome from "./Pages/Welcome.tsx";
import Checkout from "./Pages/payments/Checkout.tsx";
import Success from "./Pages/payments/Success.tsx";
import Cancel from "./Pages/payments/Cancel.tsx";

const STRIPE_PUBLISHABLE_KEY = import.meta.env.VITE_APP_STRIPE_PUBLISHABLE_KEY;
const stripePromise = loadStripe(STRIPE_PUBLISHABLE_KEY);

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
            {
                path: "/checkout",
                element: <Checkout />,
                errorElement: <ErrorPage />,
            },
            {
                path: "/success",
                element: <Success />,
                errorElement: <ErrorPage />,
            },
            {
                path: "/cancel",
                element: <Cancel />,
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
        <Elements stripe={stripePromise}>
            <AnimatePresence mode="wait" initial={true}>
                <RouterProvider router={router} />
            </AnimatePresence>
        </Elements>
    </React.StrictMode>
);
