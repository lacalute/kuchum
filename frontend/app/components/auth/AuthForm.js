'use client'

import Link from 'next/link'
import { useState } from 'react'
import './authForm.scss'

export const AuthForm = ({
  submit,
  error,
  loading,
  title = 'Вход',
  footerQuest = 'Еще нет аккаунта?',
  link = '/signup',
  footerTitle = 'Регистрация',
}) => {
  const [values, setValues] = useState({
    email: '',
    password: '',
  })

  const submitHandler = e => {
    e.preventDefault()
    submit(values)
  }

  return (
    <div className="auth">
      <form onSubmit={submitHandler} className="auth__form">
        <h1 className="auth__title">{title}</h1>
        <div className="auth__group">
          <label>
            <input
              value={values.id}
              onChange={e => setValues({ ...values, email: e.target.value })}
              className="auth__input"
              type="text"
              placeholder="Введите email"
              required
            />
          </label>
        </div>
        <div className="input__group">
          <label>
            <input
              value={values.api}
              onChange={e => setValues({ ...values, password: e.target.value })}
              className="auth__input"
              type="text"
              placeholder="Введите пароль"
              required
            />
          </label>
        </div>
        <button className="auth__btn">{loading ? 'Загрузка...' : 'Войти'}</button>

        <span className="auth__error">{error && 'Ошибка в данных авторизации'}</span>
      </form>
      <p>
        {footerQuest} <Link href={link}>{footerTitle}</Link>
      </p>
    </div>
  )
}
