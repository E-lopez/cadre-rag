import { useAppState } from '../context/AppStateContext'

export default function LoadingIndicator() {
  const { state } = useAppState()

  return (
    <div className="flex gap-2 w-full max-w-2xl items-center justify-center">
      {state.loading && (
        <div className="flex items-center gap-3 px-4 py-2 rounded-lg border border-slate-800/60 shadow-sm backdrop-blur-sm transition-all duration-300">
          {/* Micro Spinner Assembly */}
          <div className="relative flex items-center justify-center w-4 h-4">
            {/* Outer spinning accent */}
            <div className="absolute inset-0 rounded-full border-2 border-transparent border-t-indigo-500 border-r-purple-500 animate-spin"></div>
            {/* Inner pulsing dot */}
            <div className="w-1 h-1 rounded-full bg-indigo-400 animate-pulse"></div>
          </div>
          
          {/* Animated Text */}
          <span className="text-xs font-medium tracking-wide text-slate-400 animate-pulse">
            Searching knowledge base…
          </span>
        </div>
      )}
    </div>
  )
}
