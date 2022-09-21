import { useEffect, useRef, useState } from "react";
import { useForm } from 'react-hook-form'
import { useSelector, useDispatch } from "react-redux"
import { createUser, loginUser } from "../../store/slices/user/services";
import { useNavigate } from "react-router-dom";
import "./Logins.css";

function Login() {
  const { register, formState:{ errors }, handleSubmit} = useForm()
  const { register:reg, setError:setErrorL , formState:{errors:errorsL}, handleSubmit:submitLogin } = useForm()

  const [e, setE] = useState(false)
  const dispatch = useDispatch()
  const to = useNavigate()

  const fatherBgRef = useRef()
  const signRef = useRef()
  const btnRef = useRef()
  const bgRef = useRef()

  const handleBackground = () =>{
    btnRef.current.classList.toggle("signing-up")
    signRef.current.classList.toggle("init-animation")
    signRef.current.classList.contains("init-animation")
    ?fatherBgRef.current.scrollTo({ behavior: "smooth", left: bgRef.current.clientWidth })
    :fatherBgRef.current.scrollTo({ behavior: "smooth", left: 100 });
  }
    
  useEffect(() => {
    bgRef.current.style.width = `${signRef.current.offsetWidth}px`;
    handleBackground();
  },[dispatch])

  const onSubmit = (data) =>{
    dispatch(createUser(data))
    to('/')
  }

  const onLogin = (data) =>{
    setE(loginUser(data))
    to('/')
  }

  return (
    <div className="wrap-sign">
      <section ref={signRef} className="sign">
        <section className="sign__user">
          <div className="sign__forms">
            <form className="sign__up" onSubmit={handleSubmit(onSubmit)}>
              <h1 className="sign__title">Create Account</h1>
              <div className="sign__icons">
                <i className="fa-brands fa-facebook"></i>
                <i className="fa-brands fa-twitter"></i>
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errors.firstName?.type === 'required' && "This field is required"}
                  {errors.firstName?.type === 'minLength' && "The min lenght is 5"}
                </span>
                <input placeholder="First Name" type="text" {...register('firstName',{required:true, minLength:5, maxLength:150})} />
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errors.lastName?.type === 'required' && "This field is required"}
                  {errors.lastName?.type === 'minLength' && "The min lenght is 5"}
                </span>
                <input placeholder="Last Name" type="text" {...register('lastName',{required:true, minLength:5, maxLength:150})} />
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errors.email?.type === 'required' && "This field is required"}
                </span>
                <input placeholder="Email" type="email" {...register('email',{required:true})} />
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errors.password?.type === 'required' && "This field is required"}
                  {errors.password?.type === 'minLength' && "The min lenght is 10"}
                </span>
                <input
                  autoComplete="current-password"
                  placeholder="Password"
                  type="password"
                  {...register('password',{required:true, minLength:10, maxLength:128})}
                />
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errors.confirmPassword?.type === 'required' && "This field is required"}
                  {errors.confirmPassword?.type === 'minLength' && "The min lenght is 10"}
                </span>
                <input
                  autoComplete="current-password"
                  placeholder="Confirm your password"
                  type="password"
                  {...register('confirmPassword',{required:true, minLength:10, maxLength:128})}
                />
              </div>
              <button className="btn-form" type="submit">
                Sign up
              </button>
            </form>
            <form className="sign__in" onSubmit={submitLogin(onLogin)}>
              <h1 className="sign__title">Sign In to Adalene</h1>
              <div className="sign__icons">
                <i className="fa-brands fa-facebook"></i>
                <i className="fa-brands fa-twitter"></i>
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errorsL.email?.type === 'required' && "This field is required"}
                </span>
                <input placeholder="Email" type="email" {...reg('email',{required:true})}/>
              </div>
              <div className="sign__inputWrap">
                <span className="error">
                  {errorsL.password?.type === 'required' && "This field is required"}
                </span>
                <input
                  autoComplete="current-password"
                  placeholder="password"
                  type="password"
                  {...reg('password',{required:true})}
                />
              </div>
              <button className="relative btn-form" type="submit">
                Log in
                <span className="error top-full">{(e)?'Your credentials are incorrects':null}</span>
              </button>
            </form>
          </div>
        </section>
        <section ref={fatherBgRef} className="sign__welcome">
          <div ref={bgRef} className="sign__bg"></div>
        </section>
        <div className="sign__text left-txt">
          <h2>Hello, Friend</h2>
          <p>Enter your personal details and start journey with us</p>
        </div>
        <div className="sign__text right-txt">
          <h2>Welcome Back</h2>
          <p>To keep connected with us please login with your personal info</p>
        </div>
        <button type="button" onClick={handleBackground} ref={btnRef} className="btn-welcome">
          <span className="btn__in">Sign In</span>
          <span className="btn__up">Sign Up</span>
        </button>
      </section>
    </div>
  );
}

export default Login;
