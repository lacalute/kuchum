'use client'

import { useState } from 'react'
import './authForm.scss'

export const AuthForm = ({ submitHandler, error, loading, title = 'Вход', values, setValues }) => {
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
    </div>
  )
}
