import {useState} from 'react'
import {useSelector} from 'react-redux'
import Logo from '../assets/img/media/logo.png'

const Header = () => {
  const { user } = useSelector(state => state.userReducer)
  const [open, setOpen] = useState(false)
  const [showmenu, setShowMenu] = useState(false)
  const [y, setY] = useState(0)
  //console.log(y)
  window.onscroll = function() {
    let scroll = window.scrollY;
    setY(scroll)
    if(y > Number(window.innerHeight)-200){
      setOpen(true)
    }
    if(y <= 300) {
      setOpen(false)
    }
    if(open === false) {
      setShowMenu(false)
    }
  }
  return (
    <>
    <header className={`w-screen h-auto px-[50px] top-0 left-0 z-10 bg-white ${open?'-translate-y-[400px]':'translate-y-0'} fixed duration-300 overflow-x-hidden`}>
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
        <div onClick={() => setShowMenu(!showmenu)} className='relative w-16 h-16 flex md:hidden flex-col gap-3 py-3 px-1 items-center justify-center rounded-xl group'>
            <div className={`relative w-full h-1 bg-red-500 rounded-full group-hover:cursor-pointer ${showmenu?'rotate-45 translate-y-2':'rotate-0'} transition-all duration-300`}></div>
            <div className={`relative w-full h-1 bg-red-500 rounded-full group-hover:cursor-pointer ${showmenu?'hidden':'block'} transition-all duration-300`}></div>
            <div className={`relative w-full h-1 bg-red-500 rounded-full group-hover:cursor-pointer ${showmenu?'-rotate-45 -translate-y-2':'rotate-0'} transition-all duration-300`}></div>
        </div>
      </div>    
      <div className='hidden md:flex flex-shrink-0 flex-row gap-8 text-gray-400 justify-end items-center'>
      <a href=''><i className="fa-solid fa-bag-shopping"></i></a>
      {user ?<a href='/'>Login</a>:<a>{user.name}</a>}
      <i className='fas fa-bars block text-xl'></i>
      </div>
    </div> 
    <div className={`w-screen absolute top-[5.5rem] left-0 bg-white ${showmenu?'hidden -z-10':'block z-30' }`}>
      <nav className='flex flex-col lg:flex-row justify-center items-center gap-10 lg:gap-20 text-gray-400'>
        <a className='hover:text-gray-500' href=''>Home</a>
        <a className='hover:text-gray-500' href='/products'>Shop All</a>
        <a className='hover:text-gray-500' href=''>Our Story</a>
        <a className='hover:text-gray-500' href=''>Contact</a>
      </nav>
    </div> 
    </header>
  </>)
}

export default Header