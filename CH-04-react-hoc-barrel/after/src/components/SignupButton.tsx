import { useTracking } from "../tracking/useTracking";

export type SignupButtonProps = {
  source: string;
};

export function SignupButton({ source }: SignupButtonProps) {
  const { track } = useTracking("SignupButton");
  return (
    <a href="/signup" onClick={() => track({ action: "signup_click", label: source })}>
      Create an account
    </a>
  );
}
