import NextAuth from "next-auth"
import GithubProvider from "next-auth/providers/github"
export const authOptions = {
  // Configure one or more authentication providers
  providers: [
    GithubProvider({
      clientId: "Ov23ct4nsVwptrXJzyxL",
      clientSecret: "2657de95f59059a9b0fb032d7f62eefa346cab9c",
    }),
    // ...add more providers here
  ],
}
export default NextAuth(authOptions)