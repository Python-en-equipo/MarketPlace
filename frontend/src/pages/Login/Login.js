import { useEffect } from "react";
import "./Logins.css";
function Login() {
  useEffect(() => {
    const d = document;
    const $btn = d.getElementById("btn-switchTo");
    const $bg = d.getElementById("bg");
    const $fatherBg = d.getElementById("father-bg");
    const $sign = d.getElementById("sign");
    $bg.style.width = `${$sign.offsetWidth}px`;
    $btn.addEventListener("click", () => {
      $btn.classList.toggle("signing-up");
      const $sign = d.getElementById("sign");
      $sign.classList.toggle("init-animation");
      $sign.classList.contains("init-animation")
        ? $fatherBg.scrollTo({ behavior: "smooth", left: $bg.clientWidth })
        : $fatherBg.scrollTo({ behavior: "smooth", left: 100 });
    });
  }, []);
  return (
    <div className="wrap-sign">
      <section id="sign" className="sign">
        <section className="sign__user">
          <div className="sign__forms">
            <form className="sign__up">
              <h1 className="sign__title">Create Account</h1>
              <div className="sign__icons">
                <i className="fa-brands fa-facebook"></i>
                <i className="fa-brands fa-twitter"></i>
              </div>
              <div className="sign__inputWrap">
                <span></span>
                <input placeholder="Name" type="text" />
              </div>
              <div className="sign__inputWrap">
                <span></span>
                <input placeholder="Email" type="email" />
              </div>
              <div className="sign__inputWrap">
                <span></span>
                <input
                  autoComplete="current-password"
                  placeholder="Password"
                  type="password"
                />
              </div>
              <button className="btn-form" type="submit">
                Sign up
              </button>
            </form>
            <form className="sign__in">
              <h1 className="sign__title">Sign In to Adalene</h1>
              <div className="sign__icons">
                <i className="fa-brands fa-facebook"></i>
                <i className="fa-brands fa-twitter"></i>
              </div>
              <div className="sign__inputWrap">
                <span></span>
                <input placeholder="Email" type="email" />
              </div>
              <div className="sign__inputWrap">
                <span></span>
                <input
                  autoComplete="current-password"
                  placeholder="password"
                  type="password"
                />
              </div>
              <button className="btn-form" type="submit">
                Log in
              </button>
            </form>
          </div>
        </section>
        <section id="father-bg" className="sign__welcome">
          <div id="bg" className="sign__bg"></div>
        </section>
        <div className="sign__text left-txt">
          <h2>Hello, Friend</h2>
          <p>Enter your personal details and start journey with us</p>
        </div>
        <div className="sign__text right-txt">
          <h2>Welcome Back</h2>
          <p>To keep connected with us please login with your personal info</p>
        </div>
        <button type="button" id="btn-switchTo" className="btn-welcome">
          <span className="btn__in">Sign In</span>
          <span className="btn__up">Sign Up</span>
        </button>
      </section>
    </div>
  );
}

export default Login;
