import './search.scss'
import {BiSearch} from "react-icons/bi";
import {IoMdClose} from "react-icons/io";

export const Search = ({value, onChange}) => {
  return (
      <div className="search">
        <label>
          <BiSearch size={18} className='search__icon-search' />
          <input className='search__input' value={value} onChange={(e) => onChange(e.target.value)} type="text" placeholder='Поиск...'/>
          {value.length ? <IoMdClose onClick={() => onChange('')} size={18} className='search__icon-remove' /> : ''}
        </label>
      </div>
  )
}