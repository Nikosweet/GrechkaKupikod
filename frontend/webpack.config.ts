import webpack from 'webpack'
import HtmlWebpackPlugin from'html-webpack-plugin'
import MiniCssExtractPlugin from 'mini-css-extract-plugin'
import path from 'path'
import { buildWebpack } from './config/build/buildWebpack'

export interface EnvVariables{
    mode: Mode
    PORT: number
}

type Mode = 'production' | 'development'

const Paths = {
    entry: path.resolve(__dirname, 'src', 'index.tsx'),
    output: path.resolve(__dirname, 'build'),
    html: path.resolve(__dirname, 'public', 'index.html')
}

export default (env: EnvVariables) => {
    const {mode, PORT} = env
    const isDev = mode === 'development'
    const config: webpack.Configuration = buildWebpack({mode, isDev, PORT, Paths })
    
    return config;
}