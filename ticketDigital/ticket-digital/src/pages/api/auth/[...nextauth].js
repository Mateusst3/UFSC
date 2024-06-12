import NextAuth from "next-auth"
import GithubProvider from "next-auth/providers/github"
export const authOptions = {
  // Configure one or more authentication providers
  providers: [
    GithubProvider({
      clientId: process.env.NODE_ENV === "development" ? process.env.GITHUB_ID_DEV : process.env.GITHUB_ID_PROD,
      clientSecret: process.env.NODE_ENV === "development" ? process.env.GITHUB_SECRET_DEV : process.env.GITHUB_SECRET_PROD,
    }),
    // ...add more providers here
  ],
}
export default NextAuth(authOptions)