'use client'

import { AuthForm } from '@/app/components/auth/AuthForm'
import { useFetching } from '@/app/hooks/useFetching'
import {AuthService} from "@/app/service/auth.service";
import {useState} from "react";

export default function SignIn() {
  const [values, setValues] = useState({
    email: '',
    password: '',
  })
  const { loading, error, fetching } = useFetching()

  const submitHandler = e => {
    e.preventDefault()
    fetching(() => fetching(AuthService.login(values)))
  }

  return <AuthForm values={values} setValues={setValues} error={error} loading={loading} submitHandler={submitHandler} />
}
