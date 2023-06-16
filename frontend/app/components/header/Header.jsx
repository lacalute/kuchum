import './header.scss'
import Link from 'next/link'
import {GrFormAdd} from 'react-icons/gr'
import {BiCollection} from 'react-icons/bi'
import {FiUser} from 'react-icons/fi'

export const Header = () => {
  return <header className='header'>
    <div className="header__container">
      <Link href='/' className="logo">Kuchum blog</Link>
      <div className="header__controls">
        <Link className='btn btn-editor' href="/editor">
          <GrFormAdd size={20}/>
        </Link>

        <Link className='btn btn-default' href="/favorites">
          <BiCollection size={20}/>
        </Link>

        <button className='btn btn-user'>
          <FiUser size={20}/>
          <span>Yaroslav K</span>
        </button>
      </div>
    </div>
  </header>
}