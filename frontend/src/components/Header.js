import clsx from 'clsx'
import { useState } from 'react'
import {useSelector} from 'react-redux'

const Header = () => {
  const { user } = useSelector(state => state.userReducer)
  const [open, setOpen] = useState(false)
  const [showHeader, setShowHeader] = useState(false)
  const [y, setY] = useState(0)

  window.onscroll = function() {
    let scroll = window.scrollY;
    setY(scroll)
    const fixedPoint = Number(window.innerHeight) - 144
    y >= fixedPoint
    ? setShowHeader(false)
    : setShowHeader(true)
  }
  return (
    <>
    <header className={clsx('fixed top-0 left-0 w-screen translate-y-0 z-10 bg-white transition-all duration-500',{["-top-full"]: !showHeader})}>
      <div className='flex flex-row flex-shrink-0 py-2 px-5 align-middle justify-between lg:justify-center items-center'>
        <label className='hidden  lg:block lg:basis-1/3 outline-none group'>
          <span className='border-black group-focus:border-b'>
            <i className='fa-solid fa-search'></i> <input className='outline-none' type="text" placeholder="Search something"></input>
          </span>
        </label>
        <p className='basis-1/3 text-5xl text-red-500 hover:text-red-700 flex items-center md:items-end justify-between md:justify-center p-1 text-center font-thin' style={{fontFamily:'didot-w02-italic,serif', fontStyle:'oblique'}}>
        <a href=''>Adalane.</a>
        </p> 
        <label className='basis-1/3 text-right hidden lg:inline-block'>
          <button className='border border-transparent hover:border-black p-2'><i className="fa-solid fa-user mr-1.5"></i> Login</button>
        </label>
        <div onClick={() => setOpen(!open)} className='w-16 h-16 flex lg:hidden flex-col gap-3 justify-center items-center p-2 cursor-pointer'>
          <i className={clsx('relative w-full h-1 bg-black rounded-lg transition-all opacity-90 hover:opcacity-100',{["rotate-45 translate-y-2"]: open})}></i>
          <i className={clsx('relative w-full h-1 bg-black rounded-lg transition-all opacity-90 hover:opcacity-100',{["hidden"]: open })}></i>
          <i className={clsx('relative w-full h-1 bg-black rounded-lg transition-all opacity-90 hover:opcacity-100',{["-rotate-45 -translate-y-2"]: open})}></i>
        </div>
      </div>
      <div className={clsx('w-full bg-white py-6 transition-all lg:hidden',{['h-0 hidden']: !open })}>
        <nav className='mx-auto w-full max-w-lg'>
          <ul className='flex flex-col gap-6 justify-center items-center'>
          <li className='cursor-pointer capitalize'>item 01</li>
          <li className='cursor-pointer capitalize'>item 02</li>
          <li className='cursor-pointer capitalize'>item 03</li>
          <li className='cursor-pointer capitalize'>item 04</li>
          <li className='cursor-pointer capitalize'>item 05</li>
          </ul>
        </nav>
      </div>
      <div className='w-full bg-white py-6 transition-all hidden lg:block'>
        <nav className='mx-auto w-full max-w-lg'>
          <ul className='flex flex-row gap-12 justify-center items-center'>
          <li className='cursor-pointer capitalize'>item 01</li>
          <li className='cursor-pointer capitalize'>item 02</li>
          <li className='cursor-pointer capitalize'>item 03</li>
          <li className='cursor-pointer capitalize'>item 04</li>
          <li className='cursor-pointer capitalize'>item 05</li>
          </ul>
        </nav>
      </div>
    </header>
    {/* <header className={`w-screen h-auto px-[50px] top-0 left-0 z-10 bg-white ${open?'-translate-y-[400px]':'translate-y-0'} fixed duration-300 overflow-x-hidden`}>
    <div className='w-full h-[5.5rem] flex flex-col md:flex-row justify-between items-center align-middle'>
      <div className='hidden md:block'>
        <label 
          className='text-gray-400 leading-3'
          htmlFor="search">Search...</label><br/>
        <input 
          id="search"
          className='w-[220px] border-x-0 border-t-0 outline-none border-b focus:border-b-2 border-red-500 py-1' />
      </div>
      <div className='w-full h-full text-5xl text-red-500 hover:text-red-700 flex items-center md:items-end justify-between md:justify-center p-1 text-center font-thin' style={{fontFamily:'didot-w02-italic,serif', fontStyle:'oblique'}}>
        <a href=''>Adalane.</a>
      </div>    
      <div className='hidden md:flex flex-shrink-0 flex-row gap-8 text-gray-400 justify-end items-center'>
      <a href=''><i className="fa-solid fa-bag-shopping"></i></a>
      {user ?<a href='/'>Login</a>:<a>{user.name}</a>}
      <i className='fas fa-bars block text-xl'></i>
      </div>
    </div> 

    </header> */}
  </>)
}

export default Header