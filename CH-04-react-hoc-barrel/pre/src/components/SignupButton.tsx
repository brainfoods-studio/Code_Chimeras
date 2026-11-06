import { withTracking, type TrackFn } from "./withTracking";

type Props = {
  source: string;
  onTrack?: TrackFn;
};

export function SignupButtonBase({ source, onTrack }: Props) {
  return (
    <a href="/signup" onClick={() => onTrack?.({ action: "signup_click", label: source })}>
      Create an account
    </a>
  );
}

export const SignupButton = withTracking(SignupButtonBase);
