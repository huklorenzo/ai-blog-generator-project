import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000',  // ✔️ correct
});

export const generateBlog = (topic) => API.post(`/generate?topic=${topic}`);
export const getBlogs = () => API.get('/blogs');
export const deleteBlog = (id) => API.delete(`/blogs/${id}`);
