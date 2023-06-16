'use client'

import { AuthForm } from '@/app/components/auth/AuthForm'
import { useFetching } from '@/app/hooks/useFetching'
import { AuthService } from '@/app/service/auth.service'

export default function SignIn() {
  const { loading, error, fetching } = useFetching()

  const registerHandler = values => {
    fetching(() => fetching(AuthService.login(values)))
  }

  return <AuthForm error={error} loading={loading} submit={registerHandler} />
}
