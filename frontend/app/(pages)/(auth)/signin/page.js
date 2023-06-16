'use client'

import { AuthForm } from '@/app/components/auth/AuthForm'
import { useFetching } from '@/app/hooks/useFetching'

export default function SignIn() {
  const { loading, error, fetching } = useFetching()

  const submitHandler = e => {
    e.preventDefault()

    fetching(() => fetching(AuthService.login(values)))
  }

  return <AuthForm error={error} loading={loading} submitHandler={submitHandler} />
}
