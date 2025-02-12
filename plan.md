# Game Industry Reports Website

## Goal
Create a modern, responsive website that showcases the game industry reports collection with the following features:
- Browse through PDF reports with preview images
- AI-generated summaries for each report
- Folder-based navigation matching the repository structure
- Advanced filtering and search capabilities
- In-browser PDF viewer
- PDF download functionality
- Modern UI with Tailwind CSS

## Technical Stack
- Vite + React for fast development and optimal performance
- Tailwind CSS for styling
- React Router for navigation
- Zustand for state management
- PDF.js for in-browser PDF viewing
- TypeScript for type safety
- Cloudflare Pages for hosting
- Cloudflare KV for data storage
- OpenAI API for PDF summarization
- GitHub Actions for automated deployments

## Data Management
Instead of using a CSV file with hardcoded paths, we'll implement a more robust solution:

### Data Structure
```typescript
interface Report {
  id: string;
  title: string;
  path: string;
  category: string[];
  metadata: {
    author?: string;
    publishDate?: string;
    region?: string[];
    year: number;
    description?: string;
  };
  aiSummary: {
    summary: string;
    keyPoints: string[];
    generatedAt: string;
    modelVersion: string;
  };
  previewUrl: string;
  pdfUrl: string;
  size: number;
  lastModified: string;
}

interface FolderStructure {
  name: string;
  path: string;
  type: 'folder' | 'file';
  children?: FolderStructure[];
  metadata?: Report;
}
```

### Data Flow
1. GitHub Actions workflow processes PDFs and generates metadata
2. PDF content is extracted and sent to OpenAI API for summarization (using secured API key)
3. Metadata and AI summaries are stored in Cloudflare KV
4. React app fetches data from Cloudflare KV
5. Client-side caching using IndexedDB for offline support

### Security Measures
1. **API Key Management**:
   - Store OpenAI API key in GitHub Secrets
   - Use Cloudflare Workers environment variables for runtime
   - Never expose API key in client-side code
   - Rotate keys periodically

2. **Access Control**:
   - API requests only through Cloudflare Workers
   - Rate limiting on summarization endpoints
   - Request validation and sanitization
   - Audit logging for API usage

## Implementation Steps

### 1. Project Setup
- [ ] Initialize Vite + React + TypeScript project
- [ ] Install and configure Tailwind CSS
- [ ] Set up ESLint and Prettier
- [ ] Configure project structure and folders
- [ ] Add required dependencies
- [ ] Set up Cloudflare Pages project
- [ ] Configure GitHub repository secrets

### 2. Data Layer
- [ ] Create GitHub Action to process PDFs and generate metadata
- [ ] Implement PDF text extraction
- [ ] Create Cloudflare Worker for OpenAI API proxy
- [ ] Set up OpenAI API integration with secure key handling
- [ ] Set up Cloudflare KV namespace
- [ ] Implement metadata and summary storage in KV
- [ ] Create TypeScript interfaces for data structures
- [ ] Implement data fetching hooks with React Suspense
- [ ] Set up IndexedDB for client-side caching
- [ ] Create folder structure mapping utility

### 3. AI Integration
- [ ] Implement PDF text extraction utility
- [ ] Create Cloudflare Worker for OpenAI API
  - Secure API key storage
  - Request validation
  - Rate limiting
  - Error handling
- [ ] Design prompt template for consistent summaries
- [ ] Implement summary generation pipeline
- [ ] Add error handling and retry logic
- [ ] Set up summary caching and updates
- [ ] Add summary quality validation
- [ ] Implement usage monitoring and logging

### 4. State Management
- [ ] Set up Zustand store
- [ ] Create stores for:
  - Application state (theme, view preferences)
  - Search/filter state
  - Folder navigation state
  - PDF viewer state
- [ ] Implement persistence for user preferences

### 5. Components
- [ ] Layout components (Header, Footer, Sidebar)
- [ ] PDF Card component with preview image and summary
- [ ] Folder navigation component
- [ ] Search bar component
- [ ] Filter components
  - Category filters
  - Year filters
  - Region filters
- [ ] PDF viewer modal/page with summary section
- [ ] Loading states and error boundaries
- [ ] Suspense fallbacks

### 6. Features
- [ ] Implement folder-based navigation
- [ ] Add search functionality
  - Full-text search using Cloudflare KV
  - Metadata search
  - AI summary search
- [ ] Create filtering system
- [ ] Implement PDF viewer integration
- [ ] Add download functionality
- [ ] Add sorting options
- [ ] Implement responsive design

### 7. UI/UX Enhancements
- [ ] Add animations and transitions
- [ ] Implement dark/light mode
- [ ] Add loading skeletons
- [ ] Implement infinite scroll or pagination
- [ ] Add keyboard shortcuts
- [ ] Improve accessibility
- [ ] Add summary feedback mechanism

### 8. Performance Optimization
- [ ] Implement lazy loading for images
- [ ] Set up Cloudflare caching rules
- [ ] Configure IndexedDB caching
- [ ] Optimize bundle size
- [ ] Add PWA support
- [ ] Implement performance monitoring

### 9. Testing and Documentation
- [ ] Write unit tests for utilities
- [ ] Add component tests
- [ ] Create end-to-end tests
- [ ] Test AI summary quality
- [ ] Write documentation
- [ ] Add README with setup instructions

### 10. Deployment
- [ ] Configure Cloudflare Pages
- [ ] Set up GitHub Actions for CI/CD
- [ ] Configure custom domain (if needed)
- [ ] Set up monitoring and analytics
- [ ] Configure error tracking

## Folder Structure
```
src/
├── components/
│   ├── layout/
│   ├── pdf/
│   ├── search/
│   └── filters/
├── stores/
├── hooks/
│   ├── ai/
│   ├── pdf/
│   └── search/
├── utils/
├── types/
├── pages/
├── styles/
└── assets/

workers/
├── ai-proxy/
│   ├── index.ts
│   ├── middleware/
│   └── utils/
└── types/

.github/
├── workflows/
└── actions/
```

## Environment Setup

### GitHub Secrets
```
OPENAI_API_KEY=<api-key>
CF_API_TOKEN=<cloudflare-api-token>
CF_ACCOUNT_ID=<cloudflare-account-id>
```

### Cloudflare Worker Environment
```
OPENAI_API_KEY=<api-key>
MAX_REQUESTS_PER_MIN=<rate-limit>
ALLOWED_ORIGINS=<comma-separated-origins>
```

## Initial Development Focus
1. Set up project and Cloudflare integration
2. Create and configure Cloudflare Worker for AI proxy
3. Implement PDF processing and secure OpenAI integration
4. Implement metadata generation and KV storage
5. Create basic PDF card grid with previews and summaries
6. Add folder navigation
7. Implement search and filters
8. Add PDF viewer integration
9. Enhance UI and add offline support
10. Optimize performance and deploy 