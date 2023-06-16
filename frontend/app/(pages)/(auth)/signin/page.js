'use client'

import { AuthForm } from '@/app/components/auth/AuthForm'
import { useFetching } from '@/app/hooks/useFetching'

export default function SignIn() {
<<<<<<< HEAD
  const { loading, error, fetching } = useFetching()

  const submitHandler = e => {
    e.preventDefault()

    fetching(() => fetching(AuthService.login(values)))
  }

  return <AuthForm error={error} loading={loading} submitHandler={submitHandler} />
=======
  return (
    <form className="form">
      <input className="input" placeholder="Nick"></input>
      <input className="input" placeholder="Password"></input>
    </form>
  )
>>>>>>> 405d5ee89cc44b6040d251a21e647a7262b797eb
}
