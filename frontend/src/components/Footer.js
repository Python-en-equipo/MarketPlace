import React from "react";

const Footer = () => {
  return (
    <footer className="w-screen relative bottom-0 z-10">
      <div className="w-full flex flex-wrap items-center justify-center p-0 sm:px-6 sm:py-8 text-center gap-y-12 sm:gap-6">
        <p
          className="w-[200px] sm:h-[280px] text-4xl text-light-red hover:text-red-700 grid place-content-top"
          style={{ fontFamily: "didot-w02-italic,serif", fontStyle: "oblique" }}
        >
          <a href="">Adalane.</a>
        </p>
        <p className="w-[200px] sm:h-[280px] grid place-content-top gap-3">
          <li className="list-none">
            <a href="">Home</a>
          </li>
          <li className="list-none">
            <a href="">Shop All</a>
          </li>
          <li className="list-none">
            <a href="">Our Story</a>
          </li>
          <li className="list-none">
            <a href="">Our Craft</a>
          </li>
          <li className="list-none">
            <a href="">Contact</a>
          </li>
        </p>
        <p className="w-[200px] sm:h-[280px] grid place-content-top gap-3">
          <li className="list-none">
            <a href="">Home</a>
          </li>
          <li className="list-none">
            <a href="">Shop All</a>
          </li>
          <li className="list-none">
            <a href="">Our Story</a>
          </li>
          <li className="list-none">
            <a href="">Our Craft</a>
          </li>
          <li className="list-none">
            <a href="">Contact</a>
          </li>
        </p>
        <p className="w-[200px] sm:h-[280px] grid place-content-top gap-3">
          <li className="list-none">
            <a href="">Home</a>
          </li>
          <li className="list-none">
            <a href="">Shop All</a>
          </li>
          <li className="list-none">
            <a href="">Our Story</a>
          </li>
          <li className="list-none">
            <a href="">Our Craft</a>
          </li>
          <li className="list-none">
            <a href="">Contact</a>
          </li>
        </p>
        <form className="w-[200px] sm:h-[280px] flex items-center justify-center flex-col text-left">
          <label className="text-2xl font-bold tracking-[0.3rem] leading-[2] text-center">JOIN US!</label>
          <div className="">
          <label htmlFor="email">Email*</label>
          <input type="text" id="email" />
          </div>
        </form>
      </div>
      <p></p>
    </footer>
  );
};

export default Footer;
