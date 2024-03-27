

import { createBrowserRouter } from "react-router-dom";
import Layout from '../Layout/Layout';
import AuthForm from "../Pages/Auth/AuthForm";
import Chat from "../Pages/Chat/Chat";
import UserPrivateRouter from "./Private/UserPrivateRouter";



export const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout></Layout>,
        children: [
            {
                path: "",
                element: 'Home'
            },
            {
                path: "about",
                element: 'About'
            },
            {
                path: "contact",
                element: 'Contact'
            },
            {
                path: "signin",
                element: <AuthForm mode='signin' />
            },
            {
                path: "signup",
                element: <AuthForm mode='signup' />
            },
            {
                path: "chat",
                element: <UserPrivateRouter> <Chat /> </UserPrivateRouter>
            },
            {
                path: "*",
                element: 'Not found'
            }
        ]
    }
])
