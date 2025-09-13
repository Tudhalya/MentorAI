-- Initial database schema for MentorAI MVP
-- This file is executed when Postgres container starts for the first time

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Documents (uploaded PDFs)
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    filename VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Chapters within documents
CREATE TABLE chapters (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    order_num INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    UNIQUE(document_id, order_num)
);

-- Content nodes (sections, equations, figures)
CREATE TABLE nodes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    chapter_id UUID NOT NULL REFERENCES chapters(id) ON DELETE CASCADE,
    node_type VARCHAR(50) NOT NULL, -- 'text', 'equation', 'figure', 'heading'
    content TEXT,
    latex_content TEXT,
    figure_url VARCHAR(512),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better query performance
CREATE INDEX idx_chapters_document_id ON chapters(document_id);
CREATE INDEX idx_nodes_chapter_id ON nodes(chapter_id);
CREATE INDEX idx_nodes_type ON nodes(node_type);
CREATE INDEX idx_documents_created_at ON documents(created_at DESC);