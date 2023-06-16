'use client'

import { AuthForm } from '@/app/components/auth/AuthForm'
import { useFetching } from '@/app/hooks/useFetching'
import { AuthService } from '@/app/service/auth.service'

export default function SignUp() {
  const { loading, error, fetching } = useFetching()

  const loginHandler = values => {
    fetching(() => fetching(AuthService.register(values)))
  }

  return (
    <AuthForm
      footerQuest="Уже есть аккаунт?"
      link="/signin"
      footerTitle="Войти"
      title="Регистрация"
      error={error}
      loading={loading}
      submit={loginHandler}
    />
  )
}
