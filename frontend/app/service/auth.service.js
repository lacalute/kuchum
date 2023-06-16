import { instance } from '@/app/service/instance'

export class AuthService {
  static login(data) {
    const response = instance('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      data,
    })
    return response
  }
  static register(data) {
    const response = instance('/api/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      data,
    })
    return response
  }
}
