import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000',  // FastAPI backend URL
});

export const generateBlog = (topic) => API.post(`/generate?topic=${topic}`);
export const getBlogs = () => API.get('/blogs');
export const deleteBlog = (id) => API.delete(`/blogs/${id}`);
