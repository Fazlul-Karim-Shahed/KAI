import React, { useState } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { Collapse, Nav, NavItem, Navbar, NavbarBrand, NavbarToggler } from 'reactstrap';


const mapStateToProps = (state) => ({})

export const Header = (props) => {


    const [open, setOpen] = useState(false)

    const toggle = () => setOpen(!open)

    return (
        <Navbar className='px-md-0 px-lg-5 py-3' expand='md' dark color='dark'>
            <NavbarBrand className='' href='/'>KonceptTech AI</NavbarBrand>
            <NavbarToggler onClick={toggle} />
            <Collapse isOpen={open} navbar>
                <Nav className='ms-auto' navbar>
                    <NavItem className='mx-2'>
                        <Link className='text-light text-decoration-none' to='/chat'>Chat</Link>
                    </NavItem>
                    <NavItem className='mx-2'>
                        <Link className='text-light text-decoration-none' to='/about'>About</Link>
                    </NavItem>
                    <NavItem className='mx-2'>
                        {props.authenticated ? <Link className='text-light text-decoration-none' to='/logout'>Logout</Link> : <Link className='text-light text-decoration-none' to='/signin'>Login</Link>}
                    </NavItem>
                </Nav>

            </Collapse>
        </Navbar>
    )
}

export default connect(mapStateToProps)(Header)