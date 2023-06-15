import {instance} from "@/app/service/instance";

export class PostService {
  static getMyFeed() {
    const response = instance('/api/posts')
    return response
  }
}