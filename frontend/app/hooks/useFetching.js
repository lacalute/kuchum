import axios, { AxiosResponse } from 'axios'
import { useState } from 'react'

export const useFetching = () => {
  const [data, setData] = useState()
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const fetching = async (callback) => {
    setIsLoading(true)
    try {
      const response = await callback()

      if (response.status !== 200) {
        throw new Error()
      }

      setData(response.data)
    } catch (error) {
      if (axios.isAxiosError(error)) {
        setError(error?.message)
      }
    } finally {
      setIsLoading(false)
    }
  }

  return { fetching, data, error, isLoading, setData }
}