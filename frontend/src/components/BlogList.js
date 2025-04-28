import React from 'react';

import { deleteBlog } from '../api';

function BlogList({ blogs, onDelete }) {
  const handleDelete = async (id) => {
    await deleteBlog(id);
    onDelete(id);
  };

  return (
    <div>
      {blogs.map((blog) => (
        <div key={blog.id}>
          <h2>{blog.title}</h2>
          <p>{blog.content}</p>
          <button onClick={() => handleDelete(blog.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}

export default BlogList;
