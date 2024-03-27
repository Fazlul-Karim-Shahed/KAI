import { faEnvelope, faKey, faUser } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import axios from 'axios'
import { Formik } from 'formik'
import React, { useState } from 'react'
import { connect } from 'react-redux'
import { Link, useNavigate } from 'react-router-dom'
import { Input, InputGroup, InputGroupText, Toast, ToastBody, ToastHeader } from 'reactstrap'
// import Spinner from '../../Components/Spinner'
import { saveToken } from '../../Functions/AuthFunctions'
import './AuthForm.css'


const mapStateToProps = (state) => ({})

const AuthForm = (props) => {

    const [spin, setSpin] = useState(false)
    const [errorMessage, setErrorMessage] = useState('')
    const toggle = () => setSpin(false)
    const navigate = useNavigate()

    const signInUrl = process.env.REACT_APP_BACKEND + '/api/user/signin'
    const signUpUrl = process.env.REACT_APP_BACKEND + '/api/user/signup'

    return (
        <div>
            <div className='pt-2'>
                <Formik

                    initialValues={props.mode === 'signup' ? {
                        username: '',
                        email: '',
                        password: ''
                    } : {
                        email: '',
                        password: ''
                    }
                    }

                    onSubmit={
                        (values) => {

                            setSpin(true)

                            axios.post(props.mode === 'signup' ? signUpUrl : signInUrl, props.mode === 'signup' ? {
                                username: values.username,
                                email: values.email,
                                password: values.password,
                            } : {
                                email: values.email,
                                password: values.password,
                            }, {
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            })
                                .then(data => {

                                    setErrorMessage(data.data.message)
                                    if (data.data.error) throw data.data.message
                                    // else {

                                    //     setSpin(false)
                                    //     console.log(data.data)
                                    //     setErrorMessage(data.message)
                                    //     saveToken(data.value.token)
                                    //     navigate('/')
                                    //     window.location.reload(false)



                                    // }
                                })
                                .catch(err => {
                                    setErrorMessage(err)
                                    setSpin(false)
                                })



                        }
                    }

                >
                    {({ values, handleChange, handleSubmit }) => (
                        <div onClick={toggle} className='signup_form_width'>

                            <Toast className='w-100 px-2'>
                                <ToastHeader className='text-center'>{props.mode === 'signin' ? <h5 className=''>Login</h5> : <h5>Register</h5>}</ToastHeader>
                                <ToastBody>
                                    <div className="row d-flex align-items-center h-100 flex-md-row flex-column-reverse mt-md-0 mt-3">
                                        <div className="col-md-5">
                                            <img src={props.mode === 'signin' ? "/Assets/login.jpg" : "/Assets/signup.png"} className='img-fluid' alt="" />
                                        </div>
                                        <div className="col-md-7">
                                            <div className=''>
                                                <form onSubmit={handleSubmit} className='' action="">
                                                    {props.mode === 'signup' ? <InputGroup className='w-100'>
                                                        <InputGroupText><FontAwesomeIcon icon={faUser} /></InputGroupText>
                                                        <Input
                                                            onChange={handleChange}
                                                            value={values.username}
                                                            type='text'
                                                            name='username'
                                                            placeholder='User name'
                                                            className=''
                                                        />
                                                    </InputGroup> : ''}

                                                    <InputGroup className='my-3'>
                                                        <InputGroupText><FontAwesomeIcon icon={faEnvelope} /></InputGroupText>
                                                        <Input
                                                            onChange={handleChange}
                                                            value={values.email}
                                                            type='email'
                                                            name='email'
                                                            placeholder='Email'
                                                        />
                                                    </InputGroup>

                                                    <InputGroup className='my-3'>
                                                        <InputGroupText> <FontAwesomeIcon icon={faKey} /> </InputGroupText>
                                                        <Input
                                                            onChange={handleChange}
                                                            value={values.password}
                                                            type='text'
                                                            name='password'
                                                            placeholder='Password'
                                                        />
                                                    </InputGroup>
                                                    <div className='text-center text-danger my-2 fw-bolder'>{errorMessage}</div>
                                                    <div className='text-center'>
                                                        <div>
                                                            {props.mode === 'signup' ? <span className='mt-2'>Already have an account? <Link to='/signin'> Login</Link></span> : <span className='mt-2'>First time here? <Link to='/signup'>Register now</Link></span>}

                                                            {/* <Link to='/signup'>Register as Admin</Link> */}
                                                        </div> <br />
                                                        <button style={props.mode === 'signin' ? { backgroundColor: '#01b399', color: 'white' } : { backgroundColor: '#ff2b4a', color: 'white' }} className='btn px-4 pb-2 submitBtn' type="submit">{props.mode === 'signup' ? 'Register' : 'Login'}</button>
                                                    </div>

                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </ToastBody>
                            </Toast>




                        </div>
                    )}

                </Formik>

                {/* {spin ? <Spinner /> : ''} */}
            </div>
        </div>
    )
}




export default connect(mapStateToProps)(AuthForm)