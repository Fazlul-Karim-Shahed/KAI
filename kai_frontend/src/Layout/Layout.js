import React, { useEffect } from 'react'
import { connect } from 'react-redux'
import { Outlet } from 'react-router'
import Header from '../Components/Header/Header'
import { checkAuth, tokenDecode } from '../Functions/AuthFunctions'
import { AUTHENTICATION } from '../Redux/ActionTypes'

export const Layout = (props) => {

    useEffect(() => {

        checkAuth().then(auth => {

            tokenDecode().then(data => {

                props.dispatch({
                    type: AUTHENTICATION,
                    authenticated: auth,
                    decodedToken: data
                })

            })

        })

    }, [])



    return (
        <div>
            <Header></Header>
            <Outlet></Outlet>
        </div>
    )
}

const mapStateToProps = (state) => ({})

export default connect(mapStateToProps)(Layout)