import webpack from 'webpack'
import { Configuration } from 'webpack-dev-server'
import { buildPlugins } from './buildPlugins'
import { buildLoaders } from './buildLoaders'
import { buildDevServer } from './buildDevServer'
import type { EnvVariables } from '../../webpack.config'

interface Options extends EnvVariables {
    isDev: boolean
    Paths: {
        entry: string,
        output: string,
        html: string,

    }
}

export function buildWebpack(options: Options): webpack.Configuration {
    const {mode, PORT, isDev, Paths} = options
    return {
        mode: mode ?? 'development',
        entry: Paths.entry,
        output: {
            path: Paths.output,
            filename: 'bundle.[contenthash].js',
            clean: true
        },
        plugins: buildPlugins(Paths.html),
        module: {
            rules: buildLoaders(),
        },
        resolve: {
            extensions: ['.tsx', '.ts', '.js'],
        },
        devtool: isDev ? 'inline-source-map' : false,
        devServer: buildDevServer({isDev, PORT}),
    }
}