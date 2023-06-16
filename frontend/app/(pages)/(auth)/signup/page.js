'use client'

import { AuthForm } from '@/app/components/auth/AuthForm'
import { useFetching } from '@/app/hooks/useFetching'
import {useState} from "react";
import {AuthService} from "@/app/service/auth.service";

export default function SignUp() {
  const { loading, error, fetching } = useFetching()
  const [values, setValues] = useState({
    email: '',
    password: '',
  })

  const submitHandler = e => {
    e.preventDefault()

    fetching(() => fetching(AuthService.register(values)))
  }

  return <AuthForm title='Регистрация' values={values} setValues={setValues} error={error} loading={loading} submitHandler={submitHandler} />
}
