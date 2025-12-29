import webpack from 'webpack'
import HtmlWebpackPlugin from'html-webpack-plugin'
import { Configuration } from 'webpack-dev-server'
import path from 'path'

interface EnvVariables{
    mode: Mode
    PORT: number
}

type Mode = 'production' | 'development'

export default (env: EnvVariables) => {
    const isDev = env.mode === 'development'
    const config: webpack.Configuration = {
        mode: env.mode ?? 'development',
        entry: path.resolve(__dirname, 'src', 'index.tsx'),
        output: {
            path: path.resolve(__dirname, 'build'),
            filename: 'bundle.[contenthash].js',
            clean: true
        },
        plugins: [
            new HtmlWebpackPlugin({template: path.resolve(__dirname, 'public', 'index.html')})
        ],
        module: {
            rules: [
            {
                test:/\.s[ac]ss$/i,
                use: ['style-loader', 'css-loader', 'sass-loader'], 
            },
            {
                test:/\.css$/i,
                use:['style-loader', 'css-loader']
            },
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            ],
        },
        resolve: {
            extensions: ['.tsx', '.ts', '.js'],
        },
        devtool: isDev ? 'inline-source-map' : false,
        devServer: isDev ? {
            port: env.PORT || 5000,
            open: true
        } : undefined,
    }
    
    return config;
}