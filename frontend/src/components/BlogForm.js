import React from 'react';

import { useState } from 'react';
import { generateBlog } from '../api';

function BlogForm({ onNewBlog }) {
  const [topic, setTopic] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!topic.trim()) return;

    const { data } = await generateBlog(topic);
    onNewBlog(data);
    setTopic('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Enter blog topic..."
      />
      <button type="submit">Generate</button>
    </form>
  );
}

export default BlogForm;
