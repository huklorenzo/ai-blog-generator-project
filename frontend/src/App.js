import React from 'react';

import { useEffect, useState } from 'react';
import { getBlogs } from './api';
import BlogForm from './components/BlogForm';
import BlogList from './components/BlogList';

function App() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    fetchBlogs();
  }, []);

  const fetchBlogs = async () => {
    const { data } = await getBlogs();
    setBlogs(data);
  };

  const addBlog = (blog) => {
    setBlogs((prev) => [...prev, blog]);
  };

  const removeBlog = (id) => {
    setBlogs((prev) => prev.filter((blog) => blog.id !== id));
  };

  return (
    <div>
      <h1>AI Blog Generator</h1>
      <BlogForm onNewBlog={addBlog} />
      <BlogList blogs={blogs} onDelete={removeBlog} />
    </div>
  );
}

export default App;
