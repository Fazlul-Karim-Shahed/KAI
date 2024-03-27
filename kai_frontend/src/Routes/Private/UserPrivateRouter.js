

import React, { useState } from 'react'
import { connect } from 'react-redux'
import { Link, Outlet } from 'react-router-dom'

const mapStateToProps = (state) => {
    return {
        authenticated: state.authenticated,
        decodedToken: state.decodedToken
    }
}

export const UserPrivateRouter = ({ children, authenticated, decodedToken, ...rest }) => {

    return authenticated && decodedToken && decodedToken.hasOwnProperty('role') && (decodedToken.role === 'user') ?
        <div>
            <div className=''>
                <div className=''> <Outlet /></div>
            </div>
        </div> : <div className='text-3xl flex items-center justify-center h-[50vh]'>You are not authorized</div>
}




export default connect(mapStateToProps)(UserPrivateRouter)